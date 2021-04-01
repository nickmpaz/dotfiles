theme = {"name": "Material Dark"}

theme.update({
    "color0": "#212121",
    "color1": "#EF5350",
    "color2": "#CDDC39",
    "color3": "#FFCA28",
    "color4": "#64B5F6",
    "color5": "#9575CD",
    "color6": "#4DD0E1",
    "color7": "#CCCCCC",
    "color8": "#424242",
    "color9": "#E57373",
    "color10": "#DCE775",
    "color11": "#FFD54F",
    "color12": "#BBDEFB",
    "color13": "#B388FF",
    "color14": "#B2EBf2",
    "color15": "#DDDDDD",
})

theme["light_alt"] = theme["color0"]
theme["dark_alt"] = theme["color7"]

theme.update({
    "bg_primary": theme["color0"],
    "bg_primary_alt": theme["dark_alt"],
    "bg_secondary": theme["color8"],
    "bg_secondary_alt": theme["dark_alt"],
    "primary": theme["color3"],
    "primary_alt": theme["light_alt"],
    "secondary": theme["color2"],
    "secondary_alt": theme["light_alt"],
    "warning": theme["color9"],
    "warning_alt": theme["light_alt"],
    "error": theme["color1"],
    "error_alt": theme["light_alt"],
    "info": theme["color4"],
    "info_alt": theme["light_alt"],
})