from libqtile import layout
from libqtile.config import Match
from utils.theme import font
from utils.constants import Constants
from groups import groups
from keys import keys
from layouts import layouts
from screens import screens
from src.mouse import mouse
from hooks import *

groups = groups
keys = keys
layouts = layouts
screens = screens
mouse = mouse
auto_fullscreen = True
bring_front_click = False
cursor_warp = True
dgroups_key_binder = None
dgroups_app_rules = []
extension_defaults = dict(
    font=font,
    fontsize=Constants.EXTENSION_FONT_SIZE,
    padding=Constants.EXTENSION_PADDING,
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
focus_on_window_activation = "never"
follow_mouse_focus = True
widget_defaults = dict(
    font=font,
    fontsize=Constants.WIDGET_FONT_SIZE,
    padding=Constants.WIDGET_PADDING,
)
wmname = "LG3D"
