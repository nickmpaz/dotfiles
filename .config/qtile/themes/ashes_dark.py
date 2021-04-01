theme = {"name": "Ashes Dark"}

theme.update({
    "color0": "#1c2023",
    "color1": "#c7ae95",
    "color2": "#95c7ae",
    "color3": "#aec795",
    "color4": "#ae95c7",
    "color5": "#c795ae",
    "color6": "#95aec7",
    "color7": "#c7ccd1",
    "color8": "#747c84",
    "color9": "#c7ae95",
    "color10": "#95c7ae",
    "color11": "#aec795",
    "color12": "#ae95c7",
    "color13": "#c795ae",
    "color14": "#95aec7",
    "color15": "#f3f4f5"
})

theme["light_alt"] = theme["color0"]
theme["dark_alt"] = theme["color7"]

theme.update({
    "bg_primary": theme["color0"],
    "bg_primary_alt": theme["dark_alt"],
    "bg_secondary": theme["color8"],
    "bg_secondary_alt": theme["dark_alt"],
    "primary": theme["color4"],
    "primary_alt": theme["light_alt"],
    "secondary": theme["color2"],
    "secondary_alt": theme["light_alt"],
    "warning": theme["color5"],
    "warning_alt": theme["light_alt"],
    "error": theme["color13"],
    "error_alt": theme["light_alt"],
    "info": theme["color3"],
    "info_alt": theme["light_alt"],
})