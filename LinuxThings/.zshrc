if [ -f ~/.common_shellrc ]; then
  source ~/.common_shellrc
fi

export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"
export PATH="/usr/local/opt/python@3.12/bin:$PATH"
export PATH="/usr/local/opt/game-porting-toolkit/bin:$PATH"
export LDFLAGS="-L/usr/local/opt/game-porting-toolkit/lib"

if [ "$(arch)" = "arm64" ]; then
    eval "$(/opt/homebrew/bin/brew shellenv)"
else
    eval "$(/usr/local/bin/brew shellenv)"
fi

setopt prompt_subst
PROMPT='[%B%F{green}%n%b%f@%B%F{magenta}%m%b%f]-[%B%F{blue}%1~%b%f] %B%F{yellow}$(git_branch)%b%f=> '