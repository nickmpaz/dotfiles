from logging import INFO
from libqtile import bar, widget 
from libqtile.config import Screen
from libqtile.log_utils import logger

from libqtile import hook


from utils.theme import Colors

def current_layout():
    return [
        widget.TextBox(
            text='[', 
            foreground=Colors.SECONDARY_ALT, 
            background=Colors.SECONDARY
        ),
        widget.CurrentLayout(
            foreground=Colors.SECONDARY_ALT, 
            background=Colors.SECONDARY
        ),
        widget.TextBox(
            text=']', 
            foreground=Colors.SECONDARY_ALT, 
            background=Colors.SECONDARY
        ),
    ]

def group_box():
    return [
        widget.GroupBox(
            active=Colors.BG_PRIMARY_ALT,
            inactive=Colors.BG_SECONDARY,
            this_current_screen_border=Colors.PRIMARY,
            this_screen_border=Colors.PRIMARY,
            other_screen_border=Colors.SECONDARY,
            other_current_screen_border=Colors.SECONDARY,
            urgent_border=Colors.WARNING,
            padding_x=6,
        ),
    ]

def battery():
    return [
        widget.TextBox(
            text='[',
            foreground=Colors.INFO_ALT,
            background=Colors.INFO,
        ),
        widget.Battery(
            foreground=Colors.INFO_ALT,
            background=Colors.INFO,
        ),
        widget.TextBox(
            text=']',
            foreground=Colors.INFO_ALT,
            background=Colors.INFO,
        ),
    ]
def clock():
    return [
        widget.Clock(
            format='[ %A, %b %_d %Y, %I:%M:%S %p ]',
            foreground=Colors.PRIMARY_ALT,
            background=Colors.PRIMARY
        ),
    ]

def systray():
    return [
        widget.TextBox(
            text='[',
            foreground=Colors.PRIMARY_ALT,
            background=Colors.PRIMARY,
        ),
        widget.Systray(
            foreground=Colors.PRIMARY_ALT,
            background=Colors.PRIMARY,
            padding=12,
        ),
        widget.Spacer(
            length=12,
            foreground=Colors.PRIMARY_ALT,
            background=Colors.PRIMARY,
        ),
        widget.TextBox(
            text=']',
            foreground=Colors.PRIMARY_ALT,
            background=Colors.PRIMARY,
        ),
    ]

def volume():
    return [
        widget.TextBox(
            text='[',
            foreground=Colors.WARNING_ALT,
            background=Colors.WARNING,
        ),
        widget.Volume(
            foreground=Colors.WARNING_ALT,
            background=Colors.WARNING,
        ),
        widget.TextBox(
            text=']',
            foreground=Colors.WARNING_ALT,
            background=Colors.WARNING,
        ),
    ]

def top_bar(primary=False):
    widgets = []
    widgets.extend(group_box())
    widgets.extend([widget.Spacer()])
    widgets.extend(clock())
    widgets.extend([widget.Spacer()])
    widgets.extend(battery())
    widgets.extend(volume())
    widgets.extend(current_layout())
    if primary:
        widgets.extend(systray())

    return bar.Bar(
        widgets,
        32,
        background=Colors.BG_PRIMARY,
        margin=[12, 12, 0, 12],
    )

def bottom_bar(primary=False):
    widgets = []
    return bar.Bar(
        widgets,
        32,
        background=Colors.BG_PRIMARY,
    )

screens = [
    Screen(
        top=top_bar(),
    ),
    Screen(
        top=top_bar(),
    ),
    Screen(
        top=top_bar(primary=True),
    ),
]