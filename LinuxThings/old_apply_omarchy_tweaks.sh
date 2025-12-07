#!/usr/bin/env bash
# omarchy-setup.sh
# Minimal, pragmatic automation for Omarchy tweaks
set -euo pipefail

# --- CONFIGURATION (edit lists here) ---
PKGS="discord wezterm ncdu visual-studio-code-bin steam gamescope vulkan-radeon lib32-vulkan-radeon"
AUR_PKGS="zen-browser-zin tidal-hifi google-drive-ocamlfuse-git ventoy-bin"
REMOVE_PKGS="spotify 1password-cli 1password-beta aether kdenlive signal-desktop xournalpp"

# packages:
# git-lfs
# hsa-rocr
# rocm-device-libs
# rocm-smi-lib
# prism-launcher

# aur:
# packet

# github repositories to clone into ~/Documents (use full git URLs)
# Example: "https://github.com/username/repo.git"
REPOS=(
  https://github.com/Logan-Meyers/Programming2.git
  https://github.com/Logan-Meyers/PrismInstances.git
  https://github.com/Logan-Meyers/MinecraftServers.git
  https://github.com/Logan-Meyers/WSU-Obsidian-FA25.git
)

DOCUMENTS_DIR="${HOME}/Documents"
HYPR_INPUT="${HOME}/.config/hypr/input.conf"
FSTAB="/etc/fstab"
GAME_DEVICE="/dev/nvme1n1p1"
GAME_MOUNT="/mnt/GameDrive"
FSTAB_OPTS="defaults,nofail,x-systemd.device-timeout=10s"

# --- Helpers ---
info() { printf '\033[1;34m[INFO]\033[0m %s\n' "$*"; }
warn() { printf '\033[1;33m[WARN]\033[0m %s\n' "$*"; }
err() { printf '\033[1;31m[ERR]\033[0m %s\n' "$*" >&2; }
confirm() {
  local msg="${1:-Proceed? (y/N)}"
  read -r -p "$msg " yn
  case "$yn" in [Yy]*) return 0;; *) return 1;; esac
}

# --- Package installation (official) ---
install_pkgs() {
  if ! command -v pacman >/dev/null 2>&1; then
    err "pacman not found. Abort."
    return 1
  fi

  info "Installing official packages: $PKGS"
  sudo pacman -Syu --noconfirm --needed $PKGS
}

# --- AUR installation (yay/paru detection) ---
find_aur_helper() {
  if command -v yay >/dev/null 2>&1; then
    echo "yay"
  else
    echo ""
  fi
}

install_aur_pkgs() {
  local helper
  helper="$(find_aur_helper)"
  if [[ -z "$helper" ]]; then
    warn "No AUR helper (paru/yay) found. Skipping AUR installs."
    warn "Install paru or yay and rerun install_aur_pkgs."
    return 0
  fi
  info "Installing AUR packages with $helper: $AUR_PKGS"
  sudo -u "$SUDO_USER" "$helper" -S --noconfirm --needed $AUR_PKGS
}

# --- Remove unwanted packages ---
remove_pkgs() {
  info "Removing packages: $REMOVE_PKGS"
  sudo pacman -Rns --noconfirm --needed $REMOVE_PKGS || {
    warn "Some removes failed or packages not installed; continuing."
  }
  # also try AUR helper removals if present (no fail)
  local helper
  helper="$(find_aur_helper)"
  if [[ -n "$helper" ]]; then
    sudo -u "$SUDO_USER" "$helper" -R --noconfirm $REMOVE_PKGS || true
  fi
}

# --- Clone GitHub repos into Documents ---
clone_repos() {
  mkdir -p "$DOCUMENTS_DIR"
  info "Cloning repos into $DOCUMENTS_DIR"
  for repo in "${REPOS[@]}"; do
    # derive dir name from repo url
    local name
    name="$(basename -s .git "$repo")"
    local target="${DOCUMENTS_DIR}/${name}"
    if [[ -d "$target/.git" ]]; then
      info "Repo $name already exists, doing git pull (recursive)"
      git -C "$target" pull --recurse-submodules || warn "pull failed for $name"
      git -C "$target" submodule update --init --recursive || true
    else
      info "Cloning $repo -> $target"
      git clone --recurse-submodules "$repo" "$target"
    fi
  done
}

# --- Edit hypr input.conf ---
tweak_input_conf() {
  info "Tweaking $HYPR_INPUT"
  mkdir -p "$(dirname "$HYPR_INPUT")"
  touch "$HYPR_INPUT"

  # Replace a line that literally contains "# sensitivity" with "sensitivity=-0.75"
  # If the line doesn't exist, add it near top (idempotent).
  if grep -q '^# *sensitivity' "$HYPR_INPUT"; then
    # replace the first occurrence
    awk '{
      if (!done && $0 ~ /^# *sensitivity/) {
        print "sensitivity=-0.75"
        done=1
        next
      }
      print
    }' "$HYPR_INPUT" > "${HYPR_INPUT}.tmp" && mv "${HYPR_INPUT}.tmp" "$HYPR_INPUT"
  else
    # not found; put at top
    printf 'sensitivity=-0.75\n' | cat - "$HYPR_INPUT" > "${HYPR_INPUT}.tmp" && mv "${HYPR_INPUT}.tmp" "$HYPR_INPUT"
  fi

  # Add a tab-indented 'natural_scroll = true' immediately below the sensitivity line (only once)
  if grep -q $'sensitivity=-0.75\n\tnatural_scroll = true' "$HYPR_INPUT"; then
    info "natural_scroll already set."
  else
    # insert after first sensitivity line
    awk '{
      print
      if (!done && $0 ~ /^sensitivity=-0.75/) {
        print "\tnatural_scroll = true"
        done=1
      }
    }' "$HYPR_INPUT" > "${HYPR_INPUT}.tmp" && mv "${HYPR_INPUT}.tmp" "$HYPR_INPUT"
  fi

  info "Done editing $HYPR_INPUT"
}

# --- Edit btop config ---
tweak_btop_conf() {
  info "Tweaking $BTOP_CONF"
  mkdir -p "$(dirname "$BTOP_CONF")"
  touch "$BTOP_CONF"

  # Replace update_ms = 2000 with update_ms = 1000 (only first occurrence)
  if grep -q '^update_ms *= *1000' "$BTOP_CONF"; then
    info "btop update_ms already set to 1000."
    return 0
  fi

  if grep -q '^update_ms *= *2000' "$BTOP_CONF"; then
    awk '{
      if (!done && $0 ~ /^update_ms[[:space:]]*=/) {
        sub(/update_ms[[:space:]]*=[[:space:]]*2000/, "update_ms = 1000")
        done=1
      }
      print
    }' "$BTOP_CONF" > "${BTOP_CONF}.tmp" && mv "${BTOP_CONF}.tmp" "$BTOP_CONF"
    info "Replaced update_ms = 2000 -> update_ms = 1000"
  else
    # not found; add/update at top for idempotence
    printf 'update_ms = 1000\n' | cat - "$BTOP_CONF" > "${BTOP_CONF}.tmp" && mv "${BTOP_CONF}.tmp" "$BTOP_CONF"
    info "Added update_ms = 1000 to top of $BTOP_CONF"
  fi
}

# --- Add fstab entry for game drive ---
add_game_fstab() {
  if [[ ! -b "$GAME_DEVICE" ]]; then
    warn "Device $GAME_DEVICE not found (not a block device). Aborting fstab add."
    return 1
  fi

  # fetch UUID via blkid
  if ! command -v blkid >/dev/null 2>&1; then
    err "blkid not found. Install util-linux or run blkid manually."
    return 1
  fi

  local uuid
  uuid="$(blkid -s UUID -o value "$GAME_DEVICE" || true)"
  if [[ -z "$uuid" ]]; then
    err "Could not read UUID for $GAME_DEVICE. Aborting fstab add."
    return 1
  fi

  local entry="UUID=${uuid}  ${GAME_MOUNT}  ext4  ${FSTAB_OPTS}  0  2"

  # ensure mount point exists
  if [[ ! -d "$GAME_MOUNT" ]]; then
    sudo mkdir -p "$GAME_MOUNT"
    sudo chown "$USER":"$USER" "$GAME_MOUNT" || true
  fi

  # check if an entry for that UUID or mount point already exists
  if grep -q "UUID=${uuid}" "$FSTAB" || grep -q "${GAME_MOUNT}" "$FSTAB"; then
    info "fstab already contains entry for this UUID or mountpoint. Skipping append."
    return 0
  fi

  info "Appending fstab entry: $entry"
  echo "$entry" | sudo tee -a "$FSTAB" >/dev/null
  info "You can test mount with: sudo mount ${GAME_MOUNT} (or reboot)"
}

# --- install aliases for bash ---
install_aliases() {
  local script_dir source_file target bashrc zshrc dest_re

  script_dir="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" >/dev/null 2>&1 && pwd)"
  source_file="${script_dir}/.common_aliases"
  if [[ ! -f "$source_file" ]]; then
    warn "No .common_aliases at $source_file — skipping."
    return 1
  fi

  target="${HOME}/.common_aliases"
  if [[ -f "$target" && cmp -s "$source_file" "$target" ]]; then
    info ".common_aliases already up-to-date at $target"
  else
    info "Copying $source_file -> $target"
    cp "$source_file" "$target"
    chmod 644 "$target"
  fi

  # Idempotent source line regex (allow spaces/tabs)
  dest_re='^[[:space:]]*source[[:space:]]+~/.common_aliases[[:space:]]*$'
  bashrc="${HOME}/.bashrc"
  zshrc="${HOME}/.zshrc"

  # Ensure bashrc sources the aliases
  if [[ -f "$bashrc" ]]; then
    if ! grep -Eq "$dest_re" "$bashrc"; then
      info "Adding source line to $bashrc"
      printf '\n# load common aliases\nsource ~/.common_aliases\n' >> "$bashrc"
    else
      info "$bashrc already sources ~/.common_aliases"
    fi
  else
    info "Creating $bashrc and adding source line"
    printf '# ~/.bashrc\n# load common aliases\nsource ~/.common_aliases\n' > "$bashrc"
  fi

  # If user has zsh, add there too (safe/no-op if they don't use zsh)
  if [[ -f "$zshrc" ]]; then
    if ! grep -Eq "$dest_re" "$zshrc"; then
      info "Adding source line to $zshrc"
      printf '\n# load common aliases\nsource ~/.common_aliases\n' >> "$zshrc"
    else
      info "$zshrc already sources ~/.common_aliases"
    fi
  fi

  info "Aliases installed. Reload with: source ~/.bashrc"
}

# --- remove default hypr bindings I don't want ---
remove_hypr_bindings() {
  local HYPR_BINDINGS="${HOME}/.config/hypr/bindings.conf"
  local backup ts prefixes regex

  prefixes=(
    "bindd = SUPER SHIFT, G"
    "bindd = SUPER SHIFT, W"
    "bindd = SUPER SHIFT, A"
    "bindd = SUPER SHIFT ALT, A"
    "bindd = SUPER SHIFT, C"
    "bindd = SUPER SHIFT, E"
    "bindd = SUPER SHIFT, Y"
    "bindd = SUPER SHIFT ALT, G"
    "bindd = SUPER SHIFT CTRL, G"
    "bindd = SUPER SHIFT, P"
    "bindd = SUPER SHIFT, X"
    "bindd = SUPER SHIFT ALT, X"
  )

  if [[ ! -f "$HYPR_BINDINGS" ]]; then
    warn "No hypr bindings file at $HYPR_BINDINGS — nothing to do."
    return 0
  fi

  ts="$(date +%s)"
  backup="${HYPR_BINDINGS}.bak.${ts}"
  cp -- "$HYPR_BINDINGS" "$backup"
  info "Backed up original to $backup"

  # Build a single alternation regex of quoted, escaped prefixes
  regex=""
  for p in "${prefixes[@]}"; do
    # escape regex metachars
    local esc
    esc="$(printf '%s' "$p" | sed -e 's/[]\/$*.^[]/\\&/g')"
    if [[ -z "$regex" ]]; then
      regex="^[:space:]*${esc}"
    else
      regex="${regex}\|^[:space:]*${esc}"
    fi
  done

  # If no prefixes, nothing to do
  if [[ -z "$regex" ]]; then
    info "No prefixes configured; aborting."
    return 0
  fi

  # Use awk to remove any line matching any of the prefixes (leading space allowed)
  awk -v r="$regex" 'BEGIN{IGNORECASE=0} { if ($0 ~ r) next; print }' "$backup" > "${HYPR_BINDINGS}.tmp" \
    && mv "${HYPR_BINDINGS}.tmp" "$HYPR_BINDINGS"

  info "Removed matching bindings from $HYPR_BINDINGS (see backup $backup)."
}

# --- run everything ---
run_all() {
  info "Running full setup. This will require sudo for package and fstab operations."
  if ! confirm "Continue and run all steps? (y/N)"; then
    warn "Aborted by user."
    return 1
  fi

  install_pkgs
  install_aur_pkgs
  remove_pkgs
  clone_repos
  tweak_input_conf
  add_game_fstab
  install_aliases
  remove_hypr_bindings

  info "All done."
}

# --- CLI interface ---
usage() {
  cat <<EOF
Usage: $0 [command]

Commands:
  install_pkgs         Install official packages
  install_aur_pkgs     Install AUR packages (requires paru/yay)
  remove_pkgs          Remove unwanted packages
  clone_repos          Clone GitHub repos into $DOCUMENTS_DIR
  tweak_input_conf     Edit $HYPR_INPUT (sensitivity + natural_scroll)
  add_game_fstab       Add fstab entry for $GAME_DEVICE -> $GAME_MOUNT
  install_aliases      Add bash aliases
  remove_hypr_bindings Remove annoying default bindings
  run_all              Run everything (prompt)
  help                 Show this help
EOF
}

main() {
  if [[ $# -lt 1 ]]; then
    usage
    exit 1
  fi

  case "$1" in
    install_pkgs) install_pkgs ;;
    install_aur_pkgs) install_aur_pkgs ;;
    remove_pkgs) remove_pkgs ;;
    clone_repos) clone_repos ;;
    tweak_input_conf) tweak_input_conf ;;
    tweak_btop_conf) tweak_btop_conf ;;
    add_game_fstab) add_game_fstab ;;
    install_aliases) install_aliases ;;
    remove_hypr_bindings) remove_hypr_bindings ;;
    run_all) run_all ;;
    help|--help|-h) usage ;;
    *) err "Unknown command: $1"; usage; exit 2 ;;
  esac
}

main "$@"
