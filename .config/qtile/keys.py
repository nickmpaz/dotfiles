from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy
import subprocess
from utils.constants import Constants
from utils.commands import *
from groups import groups

scripts_dir = "/home/treeline/.config/qtile/scripts/"

def lazy_function(qtile, cmd):
    subprocess.Popen(cmd)


keys = [
    Key([Constants.MOD], "h", lazy.to_screen(0), desc="Move focus to screen 0"),
    Key([Constants.MOD], "l", lazy.to_screen(1), desc="Move focus to screen 1"),
    Key([Constants.MOD], "j", lazy.layout.down()),
    Key([Constants.MOD], "k", lazy.layout.up()),
    Key([Constants.MOD, "shift"], "h", lazy.layout.swap_left()),
    Key([Constants.MOD, "shift"], "l", lazy.layout.swap_right()),
    Key([Constants.MOD, "shift"], "j", lazy.layout.shuffle_down()),
    Key([Constants.MOD, "shift"], "k", lazy.layout.shuffle_up()),
    Key([Constants.MOD], "i", lazy.layout.grow()),
    Key([Constants.MOD], "o", lazy.layout.shrink()),
    Key([Constants.MOD], "n", lazy.layout.reset()),
    Key([Constants.MOD], "m", lazy.layout.maximize()),
    Key([Constants.MOD], "f", lazy.window.toggle_fullscreen()),

    KeyChord([Constants.MOD], "Return", [
        Key([], "Return", lazy.spawn(Constants.TERMINAL), desc="Launch Constants.TERMINAL"),
        Key([], "b", lazy.spawn(Constants.BROWSER), desc="Launch Browser"),
    ]),

    KeyChord([Constants.MOD], "r", [
        Key([], "c", lazy.function(lazy_function, "/home/treeline/.config/qtile/scripts/code-launcher.sh"), desc="Open a repository in $EDITOR"),
    ]),

    Key([Constants.MOD], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([Constants.MOD], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([Constants.MOD], "d", lazy.spawn(launch_application), desc="Launch an application"),

    Key([Constants.MOD, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([Constants.MOD, "control"],"q", lazy.shutdown(), desc="Shutdown Qtile"),
]

for i in groups:
    keys.extend([
        Key([Constants.MOD], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),
        Key([Constants.MOD, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])