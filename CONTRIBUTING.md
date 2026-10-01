# Contributing

This plugin is a Claude Code / Cursor plugin for monetization product squads at monday.com. It is maintained by the Growth org. This guide covers the four most common contributions: updating monday facts, updating CRO knowledge, and adding or changing a skill.

See the README's **Contributing** section for the quick-reference checklist. This file has the full reasoning and conventions behind it.

---

## Before you start

Run CI locally before touching anything:

```bash
python3 scripts/check-plugin.py
python3 scripts/lint-playbooks.py
```

Both scripts are stdlib-only and run from the repo root. Fix all errors before committing. `check-plugin.py` catches manifest drift, broken links, and skill cross-reference gaps. `lint-playbooks.py` catches playbook structure violations, stale benchmarks, and banned claims.

---

## Updating monday.com facts (`context/monday-context.md`)

1. Verify the fact against BigBrain or the canonical internal source.
2. Edit `context/monday-context.md` — update the fact, bump `last-updated`, and set `verified-against` to the tool or source you used.
3. Add a row to the changelog table at the bottom of that file.
4. Never commit a raw query result or an internal figure that isn't already in the context file.

---

## Updating CRO knowledge (`playbooks/`)

Playbooks are the shared knowledge base cited by `monetization-surface-spec` and `monetization-design-reviewer`. Never copy playbook content into a skill's own `references/` — keep it in `playbooks/` so both skills see the same version.

1. Edit or add a file in `playbooks/`.
2. Tag every claim: `[Verified]` (you can cite a primary source), `[Reported]` (published but not primary), or `[Teardown needed]` (to investigate).
3. Date every source: `Checked: YYYY-MM-DD`. CI fails on dates older than 90 days.
4. A new playbook isn't finished until it carries the mandatory AI-native reference set: Clay, Figma, ClickUp, and Claude teardowns in the standard shape. See [playbooks/README.md](playbooks/README.md).
5. Never use phrases flagged in `lint-playbooks.py`'s `BANNED` list — these are retired or fabricated claims.
6. Run `python3 scripts/lint-playbooks.py` before committing.

---

## Changing a skill

1. Keep `SKILL.md` lean and self-sufficient — its minimum must work even without `references/`.
2. Put mechanics specific to that skill in `skills/{skill-name}/references/`.
3. Put anything a second skill needs in `playbooks/` (not in a skill folder).
4. Keep the **Required context** table current: a field that silently disappears from the table will cause hallucinated assumptions at runtime.
5. Bump the `version` field in the skill's frontmatter on any change that affects output.
6. Update all four manifests (`.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `.cursor-plugin/plugin.json`, `.cursor-plugin/marketplace.json`) to the same version — `check-plugin.py` fails if they disagree.

---

## Adding a skill

A skill is a folder under `skills/` with a single `SKILL.md`. The skill system has no other convention — no required subdirectories, no required references files. What matters:

### 1. `SKILL.md` structure

```markdown
---
name: {skill-name}           ← must match the folder name exactly
description: {one paragraph} ← shown in skill listings; include trigger phrases and what it does NOT do
version: 0.1.0
---

# {Title}

**Read first:** [plugin-rules.md](../../plugin-rules.md) — the plugin-wide rules (intake, Data gate, tool names, artifact standards). Hosts don't load it automatically: read it before doing anything else in this run, unless it's already in this conversation.

## Required context
| Input | Where | Required? |
|-------|-------|-----------|
...

## Step 1 — ...
...

## Artifact: `{artifact-name}`
...
```

The "Read first" line is required — `check-plugin.py` fails without it in the first 600 characters after frontmatter.

### 2. Register the skill everywhere

`check-plugin.py` verifies all of these. CI will fail until they're all done:

| File | What to add |
|------|------------|
| `plugin-rules.md` | Row in the **Skills** table |
| `plugin-rules.md` | Entry in the **Output folder** tree for each artifact the skill produces |
| `plugin-rules.md` | Skill name in the **Data gate** "Who it applies to" paragraph (if it uses Kramer or BigBrain) |
| `README.md` | Row in the **Who does what** table |
| `README.md` | Update the `skills-N-` badge count |
| `README.md` | Entry in the folder tree |
| `skills/monetization-growth-pm/SKILL.md` | Mention in the `description` frontmatter (standalone skill list) |
| `docs/flow.svg` | Skill name in the standalone strip |

### 3. Tests

Run both CI scripts:

```bash
python3 scripts/check-plugin.py
python3 scripts/lint-playbooks.py
```

No other test infrastructure exists yet. Manual test: call the skill with a minimal prompt and verify it reads `plugin-rules.md`, asks intake in one message, and produces the artifact without hallucinating.

### 4. Release

Bump the version in all four manifests when the skill ships. Add a row to `CHANGELOG.md`.

---

## Versioning

This plugin uses a single version across all manifests. The version follows semver loosely:

- **patch** (0.x.Y): bug fixes, wording, stale fact updates
- **minor** (0.X.0): new skill, new artifact type, new playbook, significant skill behaviour change
- **major** (X.0.0): breaking change to the artifact format or intake contract that would break a downstream consumer

`check-plugin.py` fails if the four manifests disagree on version.

---

## Questions

Open an issue or reach out to the Growth org at monday.com.
