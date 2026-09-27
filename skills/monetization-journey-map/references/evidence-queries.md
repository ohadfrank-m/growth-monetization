# Evidence queries — sizing scenarios with live data

A scenario without a frequency is a guess about who matters. Size every scenario from monday's own data before the spec ranks its paths.

## Tools

The Snowflake data MCP exposes two tools. Their full names vary by environment; find them with a tool search for `data-expert-agent`.

| Tool | Use when | How |
|---|---|---|
| `data-expert-agent` | You have a business question, not the SQL | Ask in plain language. It finds the tables, uses the curated metric definitions, runs the SQL and returns a sourced answer. It returns a `jobId`: poll `check-query-status` every ≥5 s. Answers typically take 15–60 s and at most 10 min. Pass the returned `sessionId` to ask a follow-up in the same context |
| `run-sql` | You already have the SQL, e.g. re-running a query the agent wrote for a new date range | Synchronous. The Snowflake role enforces read-only access |

Prefer `data-expert-agent`: its metric definitions are curated, so "churned account" means what Data means by it. Use `run-sql` only to re-run or slice a query the agent already wrote.

## Rules

- **Aggregates only.** Ask for counts, shares and rates by segment. Never request or write user-level rows, account names, emails or IDs.
- **Show the work.** For every figure, the file records the exact question (or SQL), the source table or model the answer names, the date range, and the run date. Tag it `[Data — {source}, {date range}, run {YYYY-MM-DD}]`.
- **Say what the number counts.** Accounts vs users, gross vs net, calendar months vs rolling 30 days. When the answer's definition differs from the scenario's, say so, and ask a follow-up in the same session rather than silently using it.
  - *Worked example (checked 2026-09-27).* Asked for self-serve cancellations by tier and billing period, the agent used `bigbrain.l3.fact_accounts_arr_w_incubation_daily`, where churn = `arr_daily_change_type = 'churn'` (paying → $0 ARR) on the `no touch` channel. That counts voluntary cancels, failed payments and moves to Free together. A cancellation-flow scenario needs a follow-up on how many of those went through the cancel flow, and an involuntary-churn scenario needs the failed-payment share.
- **No figures in the repo.** Query results go only in `.monetization/` artifacts, never in this plugin's files, examples or commit messages.
- **Small segments.** If a segment has fewer than {50} accounts in the window, report it as "<50" and don't compute a rate from it.
- **Treat the numbers as internal.** The artifact is internal. Its header says so, and a figure never goes into external-facing copy without Data's sign-off.
- **Never fail silently.** If the MCP isn't connected, times out, or can't answer, write `{slot}` in the cell, add an Open item ("Data — name TBD: {the question}"), and state it in one line at the top of Scenario sizing. The rest of the journey still runs.
- **Inside a Growth PM chain**, a slow query is not a blocker. Start it at pass 1, continue mapping, and fill the cell when it returns. If it hasn't returned by the end of pass 1, slot it.

## Question templates

Fill the braces from the scenario. Ask for the last 90 days unless seasonality matters (renewals, promotions), then ask for 12 months.

| Surface | Scenario sizing questions |
|---|---|
| **Pricing page** | Weekly accounts viewing the in-app plans page, by current tier and role (admin / member). Share of those viewers who changed plan within 7 days. Share of plan changes that went through sales vs self-serve |
| **Paywall / gate** | Weekly accounts hitting the gate for {feature}, by tier and role. Share of gate hits by non-admins. Share that started a trial or upgraded within {7} days |
| **Promotion** | Accounts eligible for {offer rule} in the last campaign. Redemption share, and 90-day retention of redeemers vs a comparable non-offer group |
| **Tier upgrade** | Weekly accounts reaching {limit} (seats, automations, feature caps), by tier and billing period. Share reaching it for the first time. Share upgrading within {7} days, by role of the user who hit it |
| **Credit UI** | Monthly accounts reaching 80% and 100% of included AI credits, by tier. Share buying an extra credit bucket within {7} days of 100%. Median days between 80% and 100% |
| **Cancellation / downgrade** | Monthly self-serve cancellations by tier and billing period. Share of cancellations by stated reason. Share that downgraded instead of cancelling. Share reactivated within 90 days |
| **Trial** | Weekly trial starts by signup source. Share reaching each aha signal (first automation, first AI action, first invite — [monday-context.md](../../../context/monday-context.md)) by trial day. Trial-to-paid within {N} days, by whether the aha signal was reached |

For the IC / admin pair, always ask the role split: what share of the triggering events come from users who can't buy. That number sizes the admin-request path.

## Writing it into `00-journey.md`

```markdown
## Scenario sizing
Data: live — data-expert-agent, 2026-06-28 → 2026-09-26, run 2026-09-27 (internal)

| Scenario | Frequency | Evidence | Query | Source |
|---|---|---|---|---|
| S1 Admin cancels, price | {N}/month (Pro monthly) | {X}% of stated reasons | "Monthly self-serve cancellations by tier and billing period, last 3 months" | [Data — {model}, Jun–Sep 2026] |
| S2 IC asks admin to upgrade | {slot} | — | "Share of seat-limit hits by non-admins" | Open item O2: Data — name TBD |
```
