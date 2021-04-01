import subprocess
from libqtile import hook
from utils.commands import *

@hook.subscribe.startup_once
def startup_once():
    return

@hook.subscribe.restart
@hook.subscribe.startup
def startup():
    subprocess.Popen(start_nm_applet)
    subprocess.Popen(set_background)