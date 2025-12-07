#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

# TODO: NEED TO ADD DRY RUN SUPPORT
# TODO: NEED TO ADD SKIP SUPPORT

# ----- MAIN DEFINITIONS -----

# Define tasks (order matters)
TASKS=(
	snapper_restorepoint
	remove_webapps
	remove_pkgs
	install_pkgs
	install_aur_pkgs
	gh_auth
	clone_repos
	custom_bash_aliases
	input_conf_tweaks
	add_game_drive_automount
	custom_hypr_bindings
)

# Map: human-readable labels
declare -A TASK_LABEL=(
	[snapper_restorepoint]="Create a snapper restore point"
	[remove_webapps]="Remove all preinstalled webapps"
	[remove_pkgs]="Remove some preinstalled packages (normal & AUR)"
	[install_pkgs]="Install packages"
	[install_aur_pkgs]="Install AUR packages"
	[gh_auth]="Sign into github with gh auth"
	[clone_repos]="Clone my github repos to Documents folder"
	[input_conf_tweaks]="Apply my custom tweaks to hypr/input.conf"
	[add_game_drive_automount]="Add fstab entry for nvme1n1p1 gamedrive"
	[custom_bash_aliases]="Curl and add custom bash aliases"
	[custom_hypr_bindings]="Curl and apply custom bindings to hypr/bindings.conf"
)

# Map: function name to call
declare -A TASK_FUNC=(
	[snapper_restorepoint]=snapper_restorepoint
	[remove_webapps]=remove_webapps
	[remove_pkgs]=remove_pkgs
	[install_pkgs]=install_pkgs
	[install_aur_pkgs]=install_aur_pkgs
	[gh_auth]=gh_auth
	[clone_repos]=clone_repos
	[input_conf_tweaks]=input_conf_tweaks
	[add_game_drive_automount]=add_game_drive_automount
	[custom_bash_aliases]=custom_bash_aliases
	[custom_hypr_bindings]=custom_hypr_bindings
)

# Enabled flags (all on by default)
declare -A TASK_ENABLED
for t in "${TASKS[@]}"; do TASK_ENABLED[$t]=1; done

# ----- CUSTOM DEFINITIONS -----

REPOS=(
    https://github.com/Logan-Meyers/Programming2.git
    https://github.com/Logan-Meyers/PrismInstances.git
    https://github.com/Logan-Meyers/MinecraftServers.git
    https://github.com/Logan-Meyers/WSU-Obsidian-FA25.git
)

PKGS=(
	discord
	ncdu
	visual-studio-code-bin
	steam
	gamescope
	vulkan-radeon
	lib32-vulkan-radeon
	github-cli
  git-lfs
  prismlauncher
)
AUR_PKGS=(
	zen-browser-bin
	tidal-hifi
	ventoy-bin
  orca-slicer-bin
  oversteer
  playit-bin
  github-desktop-bin
)
REMOVE_PKGS=(
	spotify
	1password-cli
	1password-beta
	aether
	kdenlive
	signal-desktop
	xournalpp
)
REMOVE_WEBAPPS=(
    ChatGPT
    Discord
    Figma
    GitHub
    Google\ Contacts
    Google\ Messages
    Google\ Photos
    HEY
    WhatsApp
)
REPO_CLONE_DIR_PAST_HOME="Documents/"

# ----- FUNCTION HELPERS -----
info() { printf '\033[1;34m[INFO]\033[0m %s\n' "$*"; }
warn() { printf '\033[1;33m[WARN]\033[0m %s\n' "$*"; }
err() { printf '\033[1;31m[ERR]\033[0m %s\n' "$*" >&2; }
confirm() {
  local msg="${1:-Proceed? (y/N)}"
  read -r -p "$msg " yn
  case "$yn" in [Yy]*) return 0;; *) return 1;; esac
}

check_command_exist() { command -v "$1" >/dev/null 2>&1 && return 1; }

# ----- FUNCTIONS -----

snapper_restorepoint() {
	sudo snapper create
}

remove_webapps() {
	echo "> Removing ${#REMOVE_WEBAPPS[@]} webapps:"

	for webapp in ${REMOVE_WEBAPPS[@]}; do
		echo "  - ${webapp}"
	done

	if ! confirm; then
		warn "Webapp removal aborted by user"
		return 1
	fi

	for webapp in ${REMOVE_WEBAPPS[@]}; do
		omarchy-webapp-remove "${webapp}"
	done
}

remove_pkgs() {
  echo "> Removing ${#REMOVE_PKGS[@]} preinstalled packages:"
  for pkg in "${REMOVE_PKGS[@]}"; do
    echo "  - $pkg"
  done

  if ! confirm; then
    warn "Package removal aborted by user"
    return 1
  fi

  # Build list of actually installed packages
  to_remove=()
  for pkg in "${REMOVE_PKGS[@]}"; do
    if pacman -Qq "$pkg" >/dev/null 2>&1; then
      to_remove+=("$pkg")
    else
      echo "SKIP: $pkg (not installed)"
    fi
  done

  if [[ ${#to_remove[@]} -eq 0 ]]; then
    echo "Nothing to remove."
    return 0
  fi

  echo 

  # Run the removal with proper quoting
  sudo yay -Rns --noconfirm "${to_remove[@]}"
}

install_pkgs() {
	to_install=()
	for pkg in "${PKGS[@]}"; do
		if pacman -Qq "$pkg" >/dev/null 2>&1; then
			echo "SKIP: $pkg (already installed)"
		else
			to_install+=("$pkg")
		fi
	done

	echo "> Installing ${#to_install[@]} packages:"

	for pkg in "${to_install[@]}"; do
		echo "  - $pkg"
	done

	if ! confirm; then
		warn "Package installation aborted by user"
		return 1
	fi

	sudo yay -S --needed --noconfirm "${to_install[@]}"
}

install_aur_pkgs() {
	to_install=()
	for pkg in "${AUR_PKGS[@]}"; do
		if pacman -Qq "$pkg" >/dev/null 2>&1; then
			echo "SKIP: $pkg (already installed)"
		else
			to_install+=("$pkg")
		fi
	done

	echo "> Installing ${#to_install[@]} packages:"

	for pkg in "${to_install[@]}"; do
		echo "  - $pkg"
	done

	if ! confirm; then
		warn "Package installation aborted by user"
		return 1
	fi

	sudo yay -S --needed --noconfirm "${to_install[@]}"
}

gh_auth() {
	if !(command -v "gh" >/dev/null 2>&1); then
		err "github-cli needs to be installed to do this!"
	fi

	gh auth login
}

clone_repos() {
	echo "Cloning ${#REPOS[@]} repos to Documents:"

	for repo in ${REPOS[@]}; do
		echo "  - $repo"
	done

	if ! confirm; then
		warn "GitHub repo cloning aborted by user!"
		return 1
	fi

	for repo in ${REPOS[@]}; do
		local repo_name="$(basename "${repo}")"
		repo_name="${repo_name%.git}"
		info "Making dir for ${repo_name} and cloning..."
		mkdir -p ~/$REPO_CLONE_DIR_PAST_HOME$repo_name
		git clone $repo ~/$REPO_CLONE_DIR_PAST_HOME/$repo_name --recurse-submodules
	done
}

input_conf_tweaks() {
	warn "Not implemented!"
}

add_game_drive_automount() {
	warn "Not implemented!"
}

custom_bash_aliases() {
	echo "> This will curl a file from my repo into Home."
	echo "> Then, it will add a source command to .bashrc."

	if ! confirm; then
		warn "Bash alias application canceled by user."
		return 1
	fi

	if ! curl -fLo ~/.common_aliases -- "https://raw.githubusercontent.com/Logan-Meyers/Programming2/refs/heads/main/LinuxThings/.common_aliases"; then
		err "Curl failed to download common aliases!"
		return 1
	fi

	sed -i "1isource ~/.common_aliases\n" ~/.bashrc
}

custom_hypr_bindings() {
	warn "Not implemented!"
}

# ----- MAIN HELPERS -----

show_checklist() {
	echo "Toggle tasks (type number to toggle, 'r' run, 'q' quit, 'n' to select none, 'a' to select all):"
	local i=1
	for t in "${TASKS[@]}"; do
		local mark="[ ]"
		[[ ${TASK_ENABLED[$t]} -eq 1 ]] && mark="[x]"
		printf " %2d) %s %s\n" "$i" "$mark" "${TASK_LABEL[$t]}"
		((i++))
	done
}

toggle_task_by_index() {
	local idx=$1
	if (( idx < 1 || idx > ${#TASKS[@]} )); then
		echo "Invalid index"
		return
	fi
	local key=${TASKS[$((idx-1))]}
	TASK_ENABLED[$key]=$((1 - ${TASK_ENABLED[$key]}))
}

enable_all_tasks() {
  for t in "${TASKS[@]}"; do TASK_ENABLED[$t]=1; done
}

disable_all_tasks() {
  for t in "${TASKS[@]}"; do TASK_ENABLED[$t]=0; done
}

run_selected() {
  for t in "${TASKS[@]}"; do
    if [[ ${TASK_ENABLED[$t]} -eq 1 ]]; then
		local fn=${TASK_FUNC[$t]}
		info "Running: ${TASK_LABEL[$t]}"
		if ! type "$fn" >/dev/null 2>&1; then
			echo "Function $fn not found — skipping"
			continue
		fi
		"$fn" || { echo "Task $t failed"; return 1; }
    else
      	echo "Skipping: ${TASK_LABEL[$t]}"
    fi
  done
}

# --- MAIN LOOP ---
while true; do
	show_checklist
	read -r -p $'\nEnter choice: ' choice
	case "$choice" in
		r|R) run_selected; break ;;
		q|Q) echo "Aborted"; exit 0 ;;
		a|A) enable_all_tasks;;
		n|N) disable_all_tasks;;
		'' ) run_selected; break ;; # Enter = run
		*[!0-9]* ) echo "Please enter a number, r, or q" ;;
		*) toggle_task_by_index "$choice" ;;
	esac
	echo
done
