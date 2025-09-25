local wezterm = require 'wezterm'
local style = require 'wezterm_style'  -- assumes file is in same dir or lua path

local config = wezterm.config_builder()

-- merge style into config (simple copy)
for k,v in pairs(style) do
  config[k] = v
end

-- add platform-specific stuff:
config.default_prog = { "wsl.exe", "--cd", "/mnt/c/Users/lsm03" }

config.launch_menu = {
  { label = "PowerShell", args = {"powershell.exe"} },
  { label = "Git Bash", args = {"C:\\Program Files\\Git\\bin\\bash.exe", "--login", "-i"} },
  { label = "WSL", args = {"wsl.exe"} },
}

return config