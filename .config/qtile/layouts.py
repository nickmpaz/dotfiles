from libqtile import layout
from utils.theme import Colors

from custom_layouts.margin_max import MarginMax


layouts = [
    layout.MonadTall(
        border_focus=Colors.PRIMARY,
        border_normal=Colors.PRIMARY_ALT,
        border_width=3,
        margin=12,
        new_at_current=True,
    ),
    MarginMax(margin=12),
]