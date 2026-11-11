# Source Decision Policy
For every claim store: source_id, file/URL, sheet/page/line, document version, effective_date, decision_owner, approval_status, scope.
The most recent text is NOT automatically authoritative. Prefer an explicitly approved, scoped and effective decision over a superseded baseline. Resolve conflicts with PdM/BA; leave `CONFLICTED` if unclear.
Reference sources: approved requirement/AC; approved Jira comment/decision; API and design contract for its scope; business knowledge with a documented approver; observed current behavior (evidence, NOT specification).
Preserve actual acceptance criteria wording and exact Japanese messages. Distinguish Draft, Confirmed, Superseded, Conflicted. Do not invent missing thresholds, actors or policies.
