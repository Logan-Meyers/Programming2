-- Pull in the wezterm API
local wezterm = require 'wezterm'

-- This will hold the configuration.
local style = wezterm.config_builder()

-- Animaition Stuff
style.animation_fps = 75
style.font_size = 10

-- Font Things
style.font = wezterm.font 'Otonokizaka Mono II'
style.bold_brightens_ansi_colors = BrightAndBold

-- Colors
style.colors = {
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
style.default_cursor_style = 'BlinkingUnderline'
style.cursor_thickness = '200%'
style.cursor_blink_ease_in = 'EaseOut'
style.cursor_blink_ease_out = 'EaseIn'

-- Window Settings
style.window_background_opacity = 0.9
style.hide_tab_bar_if_only_one_tab = true
style.enable_scroll_bar = true
style.window_decorations = "TITLE|RESIZE"
style.window_frame = {
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
style.initial_rows = 32
style.initial_cols = 128

-- and finally, return the configuration to wezterm
return style

-- https://wezfurlong.org/wezterm/config/appearance.html#defining-your-own-colors