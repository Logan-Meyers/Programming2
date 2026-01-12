1. Install Omarchy (duh)
2. Log in, update Omarchy to latest (Omarchy Menu → Update → Omarchy)
3. Small tweaks:
	1. Setup → Input
		1. `sensitivity = -0.75`
		2. add `natural_scroll = true` under sensitivity
4. Package installation:
	1. Packages:
		- discord
		- wezterm
		- ncdu
		- visual-studio-code-bin
		- steam (alternatively Omarchy Menu → Install → Gaming → Steam)
		- gamescope
		- vulkan-radeon
		- lib32-vulkan-radeon
	2. AUR:
		- zen-browser-zin
		- tidal-hifi
		- google-drive-ocamlfuse-git
		- ventoy-bin
5. Preinstalled & Unwanted Package/App removal:
	1. webapps: all
	2. package:
		- spotify
		- 1password-cli
		- 1password-beta
		- aether
		- kdenlive
		- signal-desktop
		- xournalpp
6. Mount GameDrive Automatically:
	1. Make mount point: `sudo mkdir -p /mnt/GameDrive`
	2. Find UUID for drive: `lsblk -f`
	3. Add entry for auto-mount in fstab: `sudo nvim /etc/fstab`, navigate to bottom, and add entry replacing X's with UUID: `UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx  /mnt/GameDrive  ext4  defaults,nofail,x-systemd.device-timeout=10s  0  2`
7. Adding my configs from previous times
	1. Log into github: `gh auth login`
	2. Download personal programming repo to Documents: `cd ~/Documents && git clone https://github.com/Logan-Meyers/Programming2.git --recurse-submodules`
	3. cp wezterm config to home: `cd ~/Documents/Programming2/LinuxThings/arch/.wezterm.lua ~`
	4. download and extract fav font (otf) from https://fontstruct.com/fontstructions/show/1399210/otonokizaka-std-ii-1
	5. make needed directory: `sudo mkdir -p /usr/local/share/fonts/otf/OtonokizakaMonoII/`R
	6. copy otf to dir: `sudo cp otonokizaka-mono-ii.otf /usr/local/share/fonts/otf/OtonokizakaMonoII/`
	7. Same thing for Bookman Old Style, but ttf and from https://online-fonts.com/fonts/bookman-old-style/download
8. Gaming:
	1. To run games in their own gamescope window, add `gamescope -W 1920 -H 1080 -r 75 -f -- %command%`

---

#### Some Good Resources

I've found for related issues, processes, etc:

- Gamescope Vulkan Error: https://www.reddit.com/r/linux_gaming/comments/15s4yz0/gamescope_fails_to_start_with_vulkan_error/