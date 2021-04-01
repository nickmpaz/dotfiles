# imports 
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from utils.theme import Colors, font
from utils.contants import *



# groups
from groups import groups

# keys
from keys import keys

from layouts import layouts

# screens
from screens import screens

# mouse
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

from hooks import *

# configuration variables
auto_fullscreen = True
bring_front_click = False
cursor_warp = True
dgroups_key_binder = None
dgroups_app_rules = []
extension_defaults = dict(
    font=font,
    fontsize=extension_default_font_size,
    padding=extension_default_padding,
)
floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),
    Match(wm_class='makebranch'),
    Match(wm_class='maketag'),
    Match(wm_class='ssh-askpass'),
    Match(title='branchdialog'),
    Match(title='pinentry'),
])
focus_on_window_activation = "smart"
follow_mouse_focus = True
widget_defaults = dict(
    font=font,
    fontsize=widget_default_font_size,
    padding=widget_default_padding,
)
wmname = "LG3D"