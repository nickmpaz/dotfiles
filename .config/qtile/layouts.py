from libqtile import layout
from utils.theme import Colors
from custom.layouts.margin_max import MarginMax
from utils.constants import Constants
    
layouts = [
    layout.MonadTall(
        border_focus=Colors.BG_PRIMARY_ALT,
        border_normal=Colors.BG_SECONDARY,
        border_width=3,
        margin=Constants.MARGIN,
        new_at_current=True,
    ),
    MarginMax(margin=Constants.MARGIN),
]