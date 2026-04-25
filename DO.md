# DO.md
<!-- Mode: DO — execute task or interpret human intent -->
<!-- Budget: this file + SPRINT.md + specific task + declared files -->

## Mode detection
- TASK-ID → EXEC mode
- `idea: [text]` → create draft in docs/refinement/ → stop
- Natural language → HUMAN mode
- Nothing → pick highest-priority READY task → EXEC mode

---

## EXEC mode

1. `git pull`
2. Read task from SPRINT.md
3. Commit: IN_PROGRESS + Locked-by + Locked-at → git push
4. Read only files in task's Context-budget
5. Implement against AC only
6. Verify: `npm run build` must pass before REVIEW
7. Commit: `[prefix]: [description] [TASK-ID]`
8. Commit: REVIEW
9. Open PR

### Commit prefixes
| Prefix | When |
|--------|------|
| `feat:` | new component, service, feature |
| `fix:` | broken behavior |
| `chore:` | status, config, setup |
| `docs:` | documentation |
| `test:` | tests only |
| `ci:` | GitHub Actions |
| `data:` | seed data, schema, export script |

### When marking DONE
- Mark all AC [x]
- Add row to DONE.md: `| TASK-XXX | title | S→S | claude | Sprint 1 | date | 0 | notes |`
- Iterations = number of rework cycles (0 = first attempt accepted)

### Constraints
- Lock TTL: 1h
- Never add runtime npm dependencies beyond Angular core
- `ng build` must succeed before REVIEW
- Never merge own PR
- If AC is ambiguous: make a decision, prefix commit with `decision:`

---

## HUMAN mode

| Says | Action |
|------|--------|
| `idea: [text]` | Create `docs/refinement/IDEA-[slug].md` + commit + stop |
| "terminé [task]" | DONE + AC [x] + DONE.md + commit |
| "bloquea [task]" | BLOCKED + reason + commit |
| "mueve [task] al sprint" | BACKLOG + SPRINT updated + commit |

### Idea draft template
```markdown
# IDEA: [title]
**Created:** [ISO]
**Source:** [trigger]
**Status:** DRAFT

## Proposal
[original text]

## Gaps
<!-- THINK fills this -->

## Decision
<!-- Human: PROMOTE to TASK-XXX | REJECT: reason -->
```

---

## After every task
```
[TASK-ID] → [STATUS]
Sprint: [N] READY · [N] IN_PROGRESS · [N] DONE
Build: passing / failing
```
