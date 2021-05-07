from themes.material_dark import theme as material_dark
from themes.ashes_dark import theme as ashes_dark
from themes.chalk_dark import theme as chalk_dark
from themes.vscode import theme as vscode
import subprocess
import os
from jinja2 import FileSystemLoader, Environment
import random

themes = [
    material_dark,
    ashes_dark,
    chalk_dark,
]
theme = vscode
font = "MesloLGM Nerd Font"

class Colors():
    BLACK = theme["color0"]
    LIGHT_BLACK = theme["color8"]
    RED = theme["color1"]
    LIGHT_RED = theme["color9"]
    GREEN = theme["color2"]
    LIGHT_GREEN = theme["color10"]
    YELLOW = theme["color3"]
    LIGHT_YELLOW = theme["color11"]
    BLUE = theme["color4"]
    LIGHT_BLUE = theme["color12"]
    MAGENTA = theme["color5"]
    LIGHT_MAGENTA = theme["color13"]
    CYAN = theme["color6"]
    LIGHT_CYAN = theme["color14"]
    WHITE = theme["color7"]
    LIGHT_WHITE = theme["color15"]
    LIGHT_ALT = theme["light_alt"]
    DARK_ALT = theme["dark_alt"]
    BG_PRIMARY = theme["bg_primary"]
    BG_PRIMARY_ALT = theme["bg_primary_alt"]
    BG_SECONDARY = theme["bg_secondary"]
    BG_SECONDARY_ALT = theme["bg_secondary_alt"]
    PRIMARY = theme["primary"]
    PRIMARY_ALT = theme["primary_alt"]
    SECONDARY = theme["secondary"]
    SECONDARY_ALT = theme["secondary_alt"]
    WARNING = theme["warning"]
    WARNING_ALT = theme["warning_alt"]
    ERROR = theme["error"]
    ERROR_ALT = theme["error_alt"]
    INFO = theme["info"]
    INFO_ALT = theme["info_alt"]


def generate_themed_config(template, destination):
    templateLoader = FileSystemLoader(searchpath=os.path.expanduser("~/.config/qtile/templates"))
    templateEnv = Environment(loader=templateLoader)
    template = templateEnv.get_template(template)
    template.stream(theme).dump(destination)

generate_themed_config("alacritty.yml", os.path.expanduser( "~/.config/alacritty/alacritty.yml" ))

generate_themed_config("dunstrc", os.path.expanduser( "~/.config/dunst/dunstrc" ))
subprocess.run(["killall", "dunst"])
# subprocess.run(["notify-send", f"Updated theme to \"{theme['name']}\""])