#!/usr/bin/env bash
# setup.sh — initialize recipes repo and launch autonomous agent
# Run once from the root of the recipes repo

set -e
GREEN='\033[0;32m'; GRAY='\033[0;90m'; BOLD='\033[1m'; NC='\033[0m'

echo -e "\n  ${BOLD}recipes${NC} — ARCH autonomous setup\n"

# Git init
if [ ! -d ".git" ]; then
  git init -q
  echo -e "  ${GREEN}+${NC} git initialized"
fi

# Symlinks
for link in AGENTS.md CLAUDE.md GEMINI.md; do
  [ -e "$link" ] && rm "$link"
  ln -s docs/AGENTS.md "$link"
  echo -e "  ${GREEN}→${NC} $link"
done

# Initial .gitignore (before any npm install)
cat > .gitignore << 'EOF'
node_modules/
dist/
.angular/
*.db
.arch/
.env
EOF
echo -e "  ${GREEN}+${NC} .gitignore"

# Initial commit
git add -A
git commit -m "chore: initialize recipes with ARCH v0.2" -q
echo -e "  ${GREEN}✓${NC} Initial commit\n"

# Push instructions
echo -e "  ${BOLD}Next steps:${NC}"
echo -e ""
echo -e "  ${GRAY}1. Create GitHub repo named 'recipes' (empty, no README)${NC}"
echo -e "  ${GRAY}2. Push:${NC}"
echo -e "     git remote add origin https://github.com/valentinlineiro/recipes"
echo -e "     git push -u origin main"
echo -e ""
echo -e "  ${GRAY}3. Enable GitHub Pages in repo settings:${NC}"
echo -e "     Source: gh-pages branch"
echo -e ""
echo -e "  ${BOLD}Launch autonomous agent (mixed mode):${NC}"
echo -e ""
echo -e "  ${GRAY}# Isolate on branch${NC}"
echo -e "  git checkout -b agent/sprint-1"
echo -e ""
echo -e "  ${GRAY}# Option A — Claude Code${NC}"
echo -e "  claude --dangerously-skip-permissions \\"
echo -e "    docs/agents/THINK.md docs/SPRINT.md docs/BACKLOG.md docs/DONE.md"
echo -e ""
echo -e "  ${GRAY}# Option B — OpenCode (free models)${NC}"
echo -e "  opencode -p \"\$(cat docs/agents/THINK.md)\""
echo -e "  # then: opencode -p \"\$(cat docs/agents/DO.md) \$(cat docs/SPRINT.md)\""
echo -e ""
echo -e "  ${GRAY}# Watch progress${NC}"
echo -e "  watch -n 5 'git log --oneline -10'"
echo -e ""
echo -e "  ${BOLD}Your role (mixed mode):${NC}"
echo -e "  ${GRAY}✓ Observe commits in real time${NC}"
echo -e "  ${GRAY}✓ Merge PRs you approve${NC}"
echo -e "  ${GRAY}✗ Don't intervene in implementation${NC}"
echo -e "  ${GRAY}✗ Don't explain anything verbally${NC}"
echo -e ""
