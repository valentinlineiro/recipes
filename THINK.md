# THINK.md
<!-- Mode: THINK — session start -->
<!-- Budget: SPRINT + BACKLOG (status only) + DONE (last 5) -->
<!-- Output: terminal only -->

## What to read
1. docs/SPRINT.md — full
2. docs/BACKLOG.md — status fields only
3. docs/DONE.md — last 5 rows

---

## Checks

### Dependencies
This project has task dependencies. Before recommending next action:
- Is TASK-001 (init) DONE? If not → it blocks everything else
- Is TASK-002 (schema + seed) DONE? If not → blocks TASK-004, 005, 006
- Is TASK-004 (list component) DONE? If not → blocks TASK-005 (detail)

### System
- Stale locks (IN_PROGRESS + Locked-at > 1h) → flag
- Tasks BLOCKED with solvable reason → suggest action

### Ideas
For each IDEA in BACKLOG: promote / discard / needs

### Next action
One recommendation: TASK-ID + which files to load.

---

## Output format

```
SPRINT [N] · GREEN / AT RISK / BLOCKED

⚠  [issue] — [action]

NEXT:
  claude do [TASK-ID] — [title]
  load: [exact files]
```

---

## Constraints
- Never write to any file
- Always check dependency chain before recommending
- One next action only
