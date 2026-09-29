#!/usr/bin/env python3
"""Plugin-level consistency checks: manifests, skills, links, cross-file lists.

Run from the repo root: python3 scripts/check-plugin.py
Exit code 1 on any error. Complements scripts/lint-playbooks.py (playbook content).
"""
import glob
import json
import os
import re
import sys

errors = []


def err(msg):
    errors.append(msg)


def load_json(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        err(f"{path}: {e}")
        return None


# Manifests: valid JSON, same name and version everywhere.
claude_plugin = load_json(".claude-plugin/plugin.json")
claude_market = load_json(".claude-plugin/marketplace.json")
cursor_plugin = load_json(".cursor-plugin/plugin.json")
cursor_market = load_json(".cursor-plugin/marketplace.json")

versions, names = {}, {}
if claude_plugin:
    versions[".claude-plugin/plugin.json"] = claude_plugin.get("version")
    names[".claude-plugin/plugin.json"] = claude_plugin.get("name")
if cursor_plugin:
    versions[".cursor-plugin/plugin.json"] = cursor_plugin.get("version")
    names[".cursor-plugin/plugin.json"] = cursor_plugin.get("name")
for path, market in ((".claude-plugin/marketplace.json", claude_market), (".cursor-plugin/marketplace.json", cursor_market)):
    if not market:
        continue
    for entry in market.get("plugins", []):
        versions[f"{path} → {entry.get('name')}"] = entry.get("version")
        names[f"{path} → plugins[]"] = entry.get("name")
    meta_version = market.get("metadata", {}).get("version")
    if meta_version:
        versions[f"{path} → metadata"] = meta_version
if len(set(versions.values())) > 1:
    err("version mismatch: " + ", ".join(f"{k}={v}" for k, v in versions.items()))
if len(set(names.values())) > 1:
    err("plugin name mismatch: " + ", ".join(f"{k}={v}" for k, v in names.items()))

# Skills: frontmatter, folder name, read-first pointer.
skills = sorted(os.path.basename(os.path.dirname(p)) for p in glob.glob("skills/*/SKILL.md"))
for skill in skills:
    path = f"skills/{skill}/SKILL.md"
    text = open(path, encoding="utf-8").read()
    fm = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not fm:
        err(f"{path}: no frontmatter")
        continue
    fields = dict(re.findall(r"^(\w+):\s*(.+)$", fm.group(1), re.M))
    if fields.get("name") != skill:
        err(f"{path}: frontmatter name '{fields.get('name')}' != folder '{skill}'")
    for key in ("description", "version"):
        if key not in fields:
            err(f"{path}: frontmatter missing {key}")
    if "](../../plugin-rules.md)" not in text[: fm.end() + 600]:
        err(f"{path}: no 'Read first' pointer to plugin-rules.md right after the title")

if os.path.exists("CLAUDE.md"):
    err("CLAUDE.md at the plugin root isn't loaded by Claude Code or Cursor — keep plugin rules in plugin-rules.md")

# Every skill is named where the plugin lists its skills.
listing_files = ["README.md", "plugin-rules.md", "skills/monetization-growth-pm/SKILL.md", "docs/flow.svg"]
for f in listing_files:
    text = open(f, encoding="utf-8").read()
    for skill in skills:
        if skill == "monetization-growth-pm" and f == "skills/monetization-growth-pm/SKILL.md":
            continue
        if skill not in text:
            err(f"{f}: doesn't mention skill {skill}")

readme = open("README.md", encoding="utf-8").read()
badge = re.search(r"skills-(\d+)-", readme)
if badge and int(badge.group(1)) != len(skills):
    err(f"README.md: skills badge says {badge.group(1)}, repo has {len(skills)}")


# Relative links and anchors in Markdown.
def slug(heading):
    h = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading.strip().lower())
    h = re.sub(r"[`*_]", "", h)
    return "".join(c for c in h if c.isalnum() or c in "- ").replace(" ", "-")


anchor_cache = {}


def anchors(path):
    if path not in anchor_cache:
        found, seen, in_code = set(), {}, False
        for line in open(path, encoding="utf-8"):
            if line.startswith("```"):
                in_code = not in_code
                continue
            m = None if in_code else re.match(r"^#{1,6}\s+(.*)", line)
            if m:
                a = slug(m.group(1))
                if a in seen:
                    seen[a] += 1
                    a = f"{a}-{seen[a]}"
                else:
                    seen[a] = 0
                found.add(a)
        anchor_cache[path] = found
    return anchor_cache[path]


for md in glob.glob("**/*.md", recursive=True):
    text = re.sub(r"```.*?```", "", open(md, encoding="utf-8").read(), flags=re.S)
    text = re.sub(r"`[^`\n]*`", "", text)
    for target in re.findall(r"\]\(([^)\s]+)\)", text):
        if target.startswith(("http://", "https://", "mailto:")) or "{" in target:
            continue
        path, _, anchor = target.partition("#")
        resolved = os.path.normpath(os.path.join(os.path.dirname(md), path)) if path else md
        if not os.path.exists(resolved):
            err(f"{md}: broken link {target}")
        elif anchor and resolved.endswith(".md") and anchor not in anchors(resolved):
            err(f"{md}: broken anchor {target}")

for e in errors:
    print(f"ERROR {e}")
print(f"\n{len(errors)} error(s) — {len(skills)} skills, version {next(iter(versions.values()), '?')}")
sys.exit(1 if errors else 0)
