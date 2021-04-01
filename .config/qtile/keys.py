from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy
import subprocess
from utils.contants import *
from utils.commands import *
from groups import groups

scripts_dir = "/home/treeline/.config/qtile/scripts/"

def lazy_function(qtile, cmd):
    subprocess.Popen(cmd)


keys = [
    Key([mod], "h", lazy.to_screen(0), desc="Move focus to screen 0"),
    Key([mod], "l", lazy.to_screen(1), desc="Move focus to screen 1"),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "o", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.reset()),
    Key([mod], "m", lazy.layout.maximize()),
    Key([mod], "f", lazy.window.toggle_fullscreen()),

    KeyChord([mod], "Return", [
        Key([], "Return", lazy.spawn(terminal), desc="Launch terminal"),
        Key([], "b", lazy.spawn(browser), desc="Launch Browser"),
    ]),

    KeyChord([mod], "r", [
        Key([], "c", lazy.function(lazy_function, "/home/treeline/.config/qtile/scripts/code-launcher.sh"), desc="Open a repository in $EDITOR"),
    ]),

    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "d", lazy.spawn(launch_application), desc="Launch an application"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"],"q", lazy.shutdown(), desc="Shutdown Qtile"),
]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])