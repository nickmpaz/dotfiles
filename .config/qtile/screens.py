from libqtile import bar, widget
from libqtile.config import Screen
from utils.theme import Colors
from custom.widgets.dynamic_group_box import DynamicGroupBox
from utils.constants import Constants


def clock():
    return [
        widget.Clock(
            format='%A, %B %d, %I:%M %P',
            foreground=Colors.BG_PRIMARY_ALT,
        ),
    ]


def systray():
    return [
        widget.Systray(
            padding=12,
        ),
    ]


def top_bar(primary=False):
    widgets = []
    widgets.extend([DynamicGroupBox(
        highlight_method="text",
        padding_x=10,
        fontsize=20,
        active=Colors.BG_PRIMARY_ALT,
        inactive=Colors.BG_SECONDARY,
        this_current_screen_border=Colors.PRIMARY,
        this_screen_border=Colors.PRIMARY,
        other_screen_border=Colors.SECONDARY,
        other_current_screen_border=Colors.SECONDARY,
        urgent_border=Colors.WARNING,
    )])
    widgets.extend([widget.Spacer()])
    widgets.extend(clock())
    if primary:
        widgets.extend(systray())

    widgets.extend([widget.Spacer(
        length=12
    )])
    return bar.Bar(
        widgets,
        32,
        background=Colors.BG_PRIMARY,
        margin=[Constants.MARGIN, Constants.MARGIN, 0, Constants.MARGIN],
    )



screens = [
    Screen(
        top=top_bar(),
    ),
    Screen(
        top=top_bar(primary=True),
    ),
]
