import subprocess


def get_xresources():
    cmd = ["xrdb", "-query"]
    output = subprocess.check_output(cmd).decode()
    xresources = {line.split()[0].replace(":", ""): line.split()[1]
                  for line in output.splitlines()}
    return xresources


xresources = get_xresources()
default_color = "#000000"


class Colors():
    BG_PRIMARY = xresources.get("*.bg_primary", default_color)
    BG_PRIMARY_ALT = xresources.get("*.bg_primary_alt", default_color)
    BG_SECONDARY = xresources.get("*.bg_secondary", default_color)
    BG_SECONDARY_ALT = xresources.get("*.bg_secondary_alt", default_color)
    PRIMARY = xresources.get("*.primary", default_color)
    PRIMARY_ALT = xresources.get("*.primary_alt", default_color)
    SECONDARY = xresources.get("*.secondary", default_color)
    SECONDARY_ALT = xresources.get("*.secondary_alt", default_color)
    WARNING = xresources.get("*.warning", default_color)
    WARNING_ALT = xresources.get("*.warning_alt", default_color)
    ERROR = xresources.get("*.error", default_color)
    ERROR_ALT = xresources.get("*.error_alt", default_color)
    INFO = xresources.get("*.info", default_color)
    INFO_ALT = xresources.get("*.info_alt", default_color)