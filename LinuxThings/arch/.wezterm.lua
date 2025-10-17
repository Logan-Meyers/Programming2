-- Pull in the wezterm API
local wezterm = require 'wezterm'

-- This will hold the configuration.
local config = wezterm.config_builder()

-- disable wayland
config.enable_wayland = false

-- Animation Stuff
config.animation_fps = 75
config.font_size = 10

-- Font Things
config.font = wezterm.font 'Otonokizaka Mono II'
config.bold_brightens_ansi_colors = BrightAndBold

-- Colors
config.colors = {
    -- The default text color
    foreground = '#debee6',
    -- The default background color
    background = '#262335',

    selection_bg = '#423f4e',

    -- Color Palettes
    ansi = {
        'black',
        '#fc3f55',  -- Red
        '#00be74',  -- Green
        '#ff8947',  -- Orange
        '#0299ee',  -- Blue
        'purple',
        'teal',
        'silver',
      },
      brights = {
        'grey',
        '#ff6168',  -- Red (pink)
        '#63f1ba',  -- Lime
        '#fdd53a',  -- Yellow
        '#00faf5',  -- Blue (light)
        '#ff7dd8',  -- purple-pink-ish
        'aqua',
        'white',
      },

    -- Cursor
    cursor_fg = 'black',
    cursor_bg = '#ff7c76',

    -- Scrollbar
    scrollbar_thumb = '#3d3650',
}

-- Cursor Settings
config.default_cursor_style = 'BlinkingUnderline'
config.cursor_thickness = '200%'
config.cursor_blink_ease_in = 'EaseOut'
config.cursor_blink_ease_out = 'EaseIn'

-- Window Settings
config.window_background_opacity = 0.9
config.hide_tab_bar_if_only_one_tab = true
config.enable_scroll_bar = true
config.window_decorations = "RESIZE"
config.window_frame = {
    active_titlebar_bg = '#171520',
    inactive_titlebar_bg = '#171520',
    border_left_width = '0.3cell',
    border_right_width = '0.3cell',
    border_bottom_height = '0.2cell',
    border_top_height = '0.2cell',
    border_left_color = '#3d3650',
    border_right_color = '#3d3650',
    border_bottom_color = '#3d3650',
    border_top_color = '#3d3650',
}

-- Initial Windows
config.initial_rows = 32
config.initial_cols = 128

-- and finally, return the configuration to wezterm
return config

-- https://wezfurlong.org/wezterm/config/appearance.html#defining-your-own-colors