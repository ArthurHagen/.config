import os
import subprocess
from libqtile import bar, layout, extension, hook, qtile, widget
from qtile_extras import widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal


mod = "mod4"
terminal = guess_terminal()

####AUTOSTART####
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])


keys = [
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl -d intel_backlight s 5%+")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl -d intel_backlight s 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer -i 5")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer -d 5")),
    Key([], "XF86AudioMute", lazy.spawn("pamixer -t")),
    Key([], "XF86AudioPrev", lazy.spawn("/home/arthurhagen/.config/qtile/rotate.sh 1024x600")), #rotates 2. display
    #Key([], "XF86AudioNext", lazy.spawn("/home/arthurhagen/.config/qtile/rotate.sh 1920x1080")), #rotates 2. display

    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    #Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("dmenu_run"), desc="Spawn dmenu"),
    Key([mod], "p", lazy.spawn("rofi -show drun"), desc="Spawn a rofi application launcher")
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus="#48f3ff", border_normal="#000000", border_width=1),
    layout.Max(margin = 5, border_focus="#48f3ff", border_width=1),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

#### MOUSE CALLBACKS ####
@lazy.function
def launch_powermenu(qtile):
    qtile.cmd_spawn('rofi -show power-menu -modi power-menu:/home/arthurhagen/.config/qtile/rofi/rofi-power-menu/rofi-power-menu')

#### WIDGETS ####
screens = [ ##B5FAFF
    Screen(#SCREEN1
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    scale=0.8,
                    custom_icon_paths="~/.config/qtile/layout-icons",
                ),
                widget.GroupBox(
                    active="#48f3ff",
                    disable_drag=True,
                    highlight_method="border",
                    #background="#000000",
                    this_current_screen_border="#48f3ff",
                    borderwidth=2,
                ),
                widget.TaskList(
                    foreground="#48f3ff",
                    #background="#48f3ff",
                    border="#48f3ff",
                    borderwidth=2,
                ),
                widget.Spacer(length=10),
                widget.Systray(),
                widget.Image(
                    filename='~/.config/qtile/icons/brightness.png',
                ),
                
                widget.Backlight(backlight_name='intel_backlight',
                    foreground="#48f3ff",
                    #background="#000000",
                ),
                widget.Spacer(length=10),
                widget.Image(
                    filename='~/.config/qtile/icons/sound.png',
                ),
                widget.PulseVolume(
                    foreground="#48f3ff",
                    #background="#000000",
                    mouse_callbacks = {'Button1': lazy.spawn(["pavucontrol"])},
                ),
                widget.Spacer(length=10),
                widget.Image(
                    filename='~/.config/qtile/icons/battery.png',
                ),
                widget.Battery(
                    format='{char} {percent:2.0%} {hour:d}:{min:02d}',
                    foreground="#48f3ff",
                    #background="#000000",
                ),
                widget.Spacer(length=10),
                widget.WiFiIcon(
                    active_colour="#48f3ff",
                    #background="#000000"
                ),
                widget.Wlan(
                    format='{essid}',
                    foreground="#48f3ff",
                    #background="#000000",
                ),
                widget.Spacer(length=10),
                widget.Image(
                    filename='~/.config/qtile/icons/calendar.png',
                    scale=True,
                    margin_x=1.8,
                    margin_y=1.8,
                ),
                widget.Clock(
                    foreground="#48f3ff",
                    #background="#000000",
                    format="%d-%m-%Y %H:%M",
                ),
                widget.Spacer(length=10),
                widget.Image(
                    filename='~/.config/qtile/icons/power.png',
                    mouse_callbacks = {'Button1': launch_powermenu},
                ),
            ],
            24,
            #border_width=[1, 1, 1, 1],
            #border_color=["#00000000", "#00000000", "#00000000", "#00000000"],
            background="#00000000"
        ),
    ),
    Screen(#SCREEN2
        top=bar.Bar([
            widget.CurrentLayoutIcon(
                    scale=0.8,
                    foreground="#48f3ff"
                ),
                widget.GroupBox(
                    foreground="#48f3ff",
                    background="#000000",
                ),
                widget.TaskList(
                    foreground="#48f3ff",
                    #background="#48f3ff",
                ),
        ],
        24,
        background="#00000000",
        )
    )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = True
cursor_warp = True
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="Tor Browser"),
        Match(title="conky")
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"