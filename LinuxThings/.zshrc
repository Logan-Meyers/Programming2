export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"
export PATH="/usr/local/opt/python@3.12/bin:$PATH"

if [ "$(arch)" = "arm64" ]; then
    eval "$(/opt/homebrew/bin/brew shellenv)"
else
    eval "$(/usr/local/bin/brew shellenv)"
fi

export PATH="/usr/local/opt/game-porting-toolkit/bin:$PATH"
export LDFLAGS="-L/usr/local/opt/game-porting-toolkit/lib"

alias pyvenv="source ~/Desktop/Programming2/PyVenv/venv/bin/activate"
alias cdprog="cd ~/Desktop/Programming2/"
alias gitqcomm='cdprog; git status; git add .; git commit -m "Updated Submodules" && git push'
alias finder="open $1"
alias tidalpy="pyvenv; tidal-dl"
alias tallylines='function _tallylines() { find "$1" -type f -exec cat {} + | wc -l; }; _tallylines'export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"
export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"

git_branch() {
  # Check if the current directory is part of a Git repository
  if git rev-parse --is-inside-work-tree &>/dev/null; then
    # Fetch the current branch name
    branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)
    if [ -n "$branch" ]; then
      echo -e "($branch) "
    fi
  fi
}

setopt prompt_subst
PROMPT='[%B%F{green}%n%b%f@%B%F{magenta}%m%b%f]-[%B%F{blue}%1~%b%f] %B%F{yellow}$(git_branch)%b%f=> '