theme = {"name": "Chalk Dark"}

theme.update({
    "color0": "#151515",
    "color1": "#fb9fb1",
    "color2": "#acc267",
    "color3": "#ddb26f",
    "color4": "#6fc2ef",
    "color5": "#e1a3ee",
    "color6": "#12cfc0",
    "color7": "#d0d0d0",
    "color8": "#505050",
    "color9": "#fb9fb1",
    "color10": "#acc267",
    "color11": "#ddb26f",
    "color12": "#6fc2ef",
    "color13": "#e1a3ee",
    "color14": "#12cfc0",
    "color15": "#f5f5f5"
})

theme["light_alt"] = theme["color0"]
theme["dark_alt"] = theme["color7"]

theme.update({
    "bg_primary": theme["color0"],
    "bg_primary_alt": theme["dark_alt"],
    "bg_secondary": theme["color8"],
    "bg_secondary_alt": theme["dark_alt"],
    "primary": theme["color1"],
    "primary_alt": theme["light_alt"],
    "secondary": theme["color6"],
    "secondary_alt": theme["light_alt"],
    "warning": theme["color5"],
    "warning_alt": theme["light_alt"],
    "error": theme["color1"],
    "error_alt": theme["light_alt"],
    "info": theme["color4"],
    "info_alt": theme["light_alt"],
})