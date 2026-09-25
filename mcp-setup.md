# MCP setup

The plugin works best with these MCP servers connected. Every skill degrades gracefully if one is missing and tells you what's affected.

| MCP | Required? | Used by |
|-----|----------|---------|
| monday.com | Recommended | `monetization-intelligence` — logging research to the Pricing Intelligence board (it asks first) |
| PricingSaaS | Recommended | `monetization-intelligence` |
| Figma | Optional | `monetization-surface-spec`, `monetization-design-reviewer` |
| Slack | Optional | `monetization-intelligence` weekly digest |
| Web search | Built in (needed for enrichment) | All skills — enrichment and surface benchmarks |

---

## monday.com

**URL:** `https://mcp.monday.com/mcp`

- **Claude.ai / Claude Desktop:** Settings → Connectors → add monday.com
- **Claude Code:** `claude mcp add --transport http monday https://mcp.monday.com/mcp`
- **Cursor:** add to `~/.cursor/mcp.json` (see snippet below)

Used to log research outputs to a **Pricing Intelligence** board — the skill offers after each output and logs on a yes (the board is created on first use; you'll be asked which workspace). Without it, artifacts are saved locally only.

---

## PricingSaaS

**URL:** `https://mcp.pricingsaas.com` · Account and API key: [pricingsaas.com](https://pricingsaas.com)

- **Claude.ai / Claude Desktop:** Settings → Connectors → add custom connector with the URL above
- **Claude Code:** `claude mcp add --transport http pricingsaas https://mcp.pricingsaas.com`
- **Cursor:** see snippet below

Some tools cost PricingSaaS credits. The skill always states the cost and waits for your confirmation. Without this MCP, `monetization-intelligence` runs in enrichment-only mode (Wayback Machine, changelogs, web, community sources).

**Verify:** ask Claude to run `get_status()` — it should return your account and credit balance.

---

## Figma

**URL:** `https://mcp.figma.com/mcp`

- **Claude.ai / Claude Desktop:** Settings → Connectors → add Figma
- **Claude Code:** `claude mcp add --transport http figma https://mcp.figma.com/mcp`

Used when you paste a Figma link into a spec or review. Without it, share a screenshot instead.

---

## Slack

**URL:** `https://mcp.slack.com/mcp`

Used only for the weekly pricing digest, which the skill formats as a paste-ready Slack message. Without it, the digest is delivered in chat.

---

## Web search

Built into Claude.ai, Claude Desktop, and Claude Code. In Cursor, make sure web search is enabled for the agent.

---

## Cursor config snippet

```json
{
  "mcpServers": {
    "monday": { "url": "https://mcp.monday.com/mcp" },
    "pricingsaas": { "command": "npx", "args": ["-y", "mcp-remote", "https://mcp.pricingsaas.com"] },
    "figma": { "url": "https://mcp.figma.com/mcp" }
  }
}
```
