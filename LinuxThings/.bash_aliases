alias pyvenv="source ~/Desktop/Programming2/PyVenv/venv/bin/activate"
alias cdprog="cd ~/Desktop/Programming2"

# personal git shortcuts
alias gst="git status"
alias gfp="git fetch && git pull"
# function to git add all, commit with passed along message, and push if successful
gacp() {
  if [ $# -eq 0 ]; then
    echo "Error: Commit message required."
    return 1
  fi
  git add .
  git commit -m "$*"
  git push
}

# USER DEFINED GIT BRANCH GETTER FOR PS1
git_branch() {
  # Check if we're in a Git repo
  branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)
  if [ -n "$branch" ]; then
    echo -e "─[\e[1;33m$branch\e[0m]"  # Yellow for branch name
  fi
}
