#!/usr/bin/env python3
"""Lint playbooks/ against the standard in playbooks/README.md.

Errors fail the run (exit 1); warnings are printed but don't.
Stdlib only. Run from the repo root: python3 scripts/lint-playbooks.py
"""
import datetime
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PLAYBOOKS = ROOT / "playbooks"
NOT_PLAYBOOKS = {"README.md", "cases.md"}

# Section order from playbooks/README.md "Playbook structure — every file".
ORDER = [
    ("Core rule", True),
    ("Benchmarks", False),
    ("Legal context", False),
    ("Patterns", True),
    ("Company teardowns", False),
    ("AI-native reference set", True),
    ("Anti-patterns", True),
    ("Copy bank", False),
    ("monday.com-specific notes", True),
    ("Sources", True),
]
AI_NATIVE = ["Clay", "Figma", "ClickUp", "Claude"]
TAGS = ("[Verified", "[Reported", "[Teardown needed")
APPLIES_TO = {"B2B SaaS", "PLG / prosumer", "consumer app", "mobile app", "publisher", "mixed", "legal"}
STALE_DAYS = 90

# Retired or fabricated claims. A line may still mention one to warn against it.
BANNED = [
    (r"1 credit\s*[≈=]\s*1 (AI )?action", "retired credit translation — use the official 1,000-credit line"),
    (r"OpenView[^.\n]{0,40}2025", "no OpenView 2025 report exists (firm closed Dec 2023)"),
    (r"ChurnZero 2025|Gainsight Customer Success Index|Totango 2025", "unsourced benchmark dropped in the fact-check"),
]
ALLOW_MENTION = re.compile(r"\b(never|not use|don't|do not|retired|dropped|wrong|reverts?|returns)\b", re.I)

errors, warnings = [], []


def err(path, line, msg):
    errors.append(f"{path.relative_to(ROOT)}:{line}: {msg}")


def warn(path, line, msg):
    warnings.append(f"{path.relative_to(ROOT)}:{line}: {msg}")


def sections(text):
    return [(i + 1, l[3:].strip()) for i, l in enumerate(text.splitlines()) if l.startswith("## ")]


def section_key(title):
    for name, _ in ORDER:
        if title.startswith(name):
            return name
    return None


def section_body(text, name):
    m = re.search(rf"^## {re.escape(name)}.*?$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return (m.group(1), text[: m.start()].count("\n") + 1) if m else (None, 0)


def check_structure(path, text):
    found = [(ln, section_key(t)) for ln, t in sections(text)]
    names = [n for _, n in found if n]
    for name, required in ORDER:
        if required and name not in names:
            err(path, 1, f"missing required section '## {name}'")
    idx = [next(i for i, (n, _) in enumerate(ORDER) if n == name) for name in names]
    for (ln, name), prev, cur in zip([f for f in found if f[1]][1:], idx, idx[1:]):
        if cur < prev:
            err(path, ln, f"section '## {name}' is out of order (see playbooks/README.md structure)")
    for ln, title in sections(text):
        if not section_key(title):
            warn(path, ln, f"section '## {title}' isn't in the standard structure")


def check_benchmarks(path, text):
    body, start = section_body(text, "Benchmarks")
    if body is None:
        return
    rows = [(start + i, l) for i, l in enumerate(body.splitlines()) if l.startswith("|")]
    if len(rows) < 3:
        err(path, start, "Benchmarks section has no table rows — remove the section if nothing qualifies")
        return
    for ln, row in rows[2:]:
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if len(cells) != 6:
            err(path, ln, f"benchmark row needs 6 columns (Metric · Number · Tag · Applies to · Source · Checked), has {len(cells)}")
            continue
        _, _, tag, applies, source, checked = cells
        if not tag.startswith(TAGS):
            err(path, ln, f"benchmark tag '{tag}' isn't an evidence tag")
        if applies not in APPLIES_TO:
            err(path, ln, f"'Applies to' value '{applies}' not in {sorted(APPLIES_TO)}")
        if "http" not in source:
            err(path, ln, "benchmark source has no URL")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", checked):
            err(path, ln, f"'Checked' must be YYYY-MM-DD, got '{checked}'")


def check_ai_native(path, text):
    heads = [t for _, t in sections(text) if t.startswith("AI-native reference set")]
    if not heads:
        return
    body, start = section_body(text, heads[0])
    subs = re.findall(r"^### (.+)$", body or "", re.M)
    for company in AI_NATIVE:
        if not any(s.startswith(company) for s in subs):
            err(path, start, f"AI-native set is missing a '### {company}' teardown")


def check_tags(path, text):
    for i, line in enumerate(text.splitlines(), 1):
        for m in re.finditer(r"\[(Ver\w*|Rep\w*|Tear\w*(?: \w+)?)", line):
            if not ("[" + m.group(1)).startswith(TAGS):
                err(path, i, f"misspelled evidence tag '[{m.group(1)}'")


def check_links(path, text, case_ids):
    for i, line in enumerate(text.splitlines(), 1):
        for target in re.findall(r"\]\(([^)\s]+)\)", line):
            if target.startswith(("http", "mailto:", "#")):
                continue
            file_part, _, anchor = target.partition("#")
            dest = (path.parent / file_part).resolve()
            if not dest.exists():
                err(path, i, f"broken link '{target}'")
            elif dest.name == "cases.md" and anchor and anchor not in case_ids:
                err(path, i, f"unknown case id '#{anchor}'")
        for cid in re.findall(r"\[case: ([\w-]+)\]", line):
            if cid not in case_ids:
                err(path, i, f"unknown case id '{cid}'")


def check_dates(path, text):
    today = datetime.date.today()
    for i, line in enumerate(text.splitlines(), 1):
        if not re.search(r"checked|Checked", line):
            continue
        for d in re.findall(r"\d{4}-\d{2}-\d{2}", line):
            try:
                age = (today - datetime.date.fromisoformat(d)).days
            except ValueError:
                err(path, i, f"invalid date '{d}'")
                continue
            if age > STALE_DAYS:
                warn(path, i, f"source checked {d} ({age} days ago) — re-verify")


def check_banned():
    files = subprocess.run(["git", "ls-files", "*.md"], cwd=ROOT, capture_output=True, text=True).stdout.split()
    for f in files:
        p = ROOT / f
        if not p.exists():
            continue
        for i, line in enumerate(p.read_text().splitlines(), 1):
            for pattern, why in BANNED:
                if re.search(pattern, line) and not ALLOW_MENTION.search(line):
                    err(p, i, why)


def main():
    case_ids = set(re.findall(r"^## ([\w-]+)$", (PLAYBOOKS / "cases.md").read_text(), re.M))
    for path in sorted(PLAYBOOKS.glob("*.md")):
        text = path.read_text()
        check_tags(path, text)
        check_links(path, text, case_ids)
        check_dates(path, text)
        if path.name in NOT_PLAYBOOKS:
            continue
        check_structure(path, text)
        check_benchmarks(path, text)
        check_ai_native(path, text)
    check_banned()

    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
