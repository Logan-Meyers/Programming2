#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

# Define tasks (order matters)
TASKS=(setup_packages install_dotfiles tweaks cleanup)

# Map: human-readable labels
declare -A TASK_LABEL=(
  [setup_packages]="Install packages"
  [install_dotfiles]="Install dotfiles"
  [tweaks]="Security & system tweaks"
  [cleanup]="Cleanup & remove unwanted packages"
)

# Map: function name to call
declare -A TASK_FUNC=(
  [setup_packages]=install_packages
  [install_dotfiles]=install_dotfiles
  [tweaks]=run_security_tweaks
  [cleanup]=remove_packages
)

# Enabled flags (all on by default)
declare -A TASK_ENABLED
for t in "${TASKS[@]}"; do TASK_ENABLED[$t]=1; done

show_checklist() {
  echo "Toggle tasks (type number to toggle, 'r' run, 'q' quit):"
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

run_selected() {
  for t in "${TASKS[@]}"; do
    if [[ ${TASK_ENABLED[$t]} -eq 1 ]]; then
      local fn=${TASK_FUNC[$t]}
      echo ">>> Running: ${TASK_LABEL[$t]}"
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

# --- Example stub functions (replace with real ones) ---
install_packages() { echo "(stub) installing packages"; sleep 1; }
install_dotfiles() { echo "(stub) installing dotfiles"; sleep 1; }
run_security_tweaks() { echo "(stub) running tweaks"; sleep 1; }
remove_packages() { echo "(stub) removing packages"; sleep 1; }

# --- Interactive loop ---
while true; do
  show_checklist
  read -r -p $'\nEnter choice: ' choice
  case "$choice" in
    r|R) run_selected; break ;;
    q|Q) echo "Aborted"; exit 0 ;;
    '' ) run_selected; break ;; # Enter = run
    *[!0-9]* ) echo "Please enter a number, r, or q" ;;
    *) toggle_task_by_index "$choice" ;;
  esac
  echo
done