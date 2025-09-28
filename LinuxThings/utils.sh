#!/bin/bash
# Usage: ./utils.sh newcdprog <new_path_segment>
# Usage: ./utils.sh updateThis
# Usage: ./utils.sh updateHome

# get system platform
unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)
        if [ -n "$WSL_INTEROP" ]; then
            platform="WSL"
        else
            platform="Linux"
        fi
        ;;
    Darwin*)
        platform="Mac"
        ;;
    *)
        platform="Unknown"
        ;;
esac

COMMON_RC="$HOME/.common_shellrc"

newcdprog() {
    if [ -z "$1" ]; then
        echo "Usage: $0 newcdprog <new_path_segment>"
        exit 1
    fi

    NEW_SEGMENT="$1"

    if [ ! -f "$COMMON_RC" ]; then
        echo "File $COMMON_RC not found."
        exit 1
    fi

    # Determine replacement path
    if [[ "$NEW_SEGMENT" == */* ]]; then
        REPLACEMENT="$NEW_SEGMENT"
    else
        REPLACEMENT="~/$NEW_SEGMENT"
    fi

    # Use sed to replace the segments in-place
    sed -i \
        -e "s|\(alias pyvenv=\"source \).*\\(/Programming2/PyVenv/venv/bin/activate\".*\)|\1$REPLACEMENT\2|" \
        -e "s|\(alias cdprog=\"cd \).*\\(/Programming2\".*\)|\1$REPLACEMENT\2|" \
        "$COMMON_RC"

    echo "Updated aliases in $COMMON_RC with segment: $REPLACEMENT"
}

updateThis() {
    SRC_BASHRC="$HOME/.bashrc"
    SRC_ZSHRC="$HOME/.zshrc"
    SRC_COMMON_RC="$HOME/.common_shellrc"
    DEST_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

    [ -f "$SRC_BASHRC" ] && cp "$SRC_BASHRC" "$DEST_DIR/.bashrc"
    [ -f "$SRC_ZSHRC" ] && cp "$SRC_ZSHRC" "$DEST_DIR/.zshrc"
    [ -f "$SRC_COMMON_RC" ] && cp "$SRC_COMMON_RC" "$DEST_DIR/.common_shellrc"
    echo "Updated files in $DEST_DIR from \$HOME."
}

updateHome() {
    SRC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    DEST_BASHRC="$HOME/.bashrc"
    DEST_ZSHRC="$HOME/.zshrc"
    DEST_COMMON_RC="$HOME/.common_shellrc"

    if [ "$platform" = "Mac" ]; then
        [ -f "$SRC_DIR/.zshrc" ] && cp "$SRC_DIR/.zshrc" "$DEST_ZSHRC"
        echo "Updated .zshrc in \$HOME from $SRC_DIR."
    else
        [ -f "$SRC_DIR/.bashrc" ] && cp "$SRC_DIR/.bashrc" "$DEST_BASHRC"
        echo "Updated .bashrc in \$HOME from $SRC_DIR."
    fi

    [ -f "$SRC_DIR/.common_shellrc" ] && cp "$SRC_DIR/.common_shellrc" "$DEST_COMMON_RC"
}

if [ "$1" = "newcdprog" ]; then
    shift
    newcdprog "$@"
elif [ "$1" = "updateThis" ]; then
    updateThis
elif [ "$1" = "updateHome" ]; then
    updateHome
else
    cat <<EOF
Usage: $0 <command> [args]

Commands:
  newcdprog <new_path_segment>
      Update the 'cdprog' and 'pyvenv' aliases in \$HOME/.common_shellrc
      to use the specified <new_path_segment> in their paths.

  updateThis
      Copy your current \$HOME/.bashrc, \$HOME/.zshrc, and \$HOME/.common_shellrc
      into the directory containing this script.

  updateHome
      Copy .bashrc, .zshrc, and .common_shellrc from this script's directory
      back to your \$HOME directory, updating your shell configuration files.

EOF
    exit 1
fi
