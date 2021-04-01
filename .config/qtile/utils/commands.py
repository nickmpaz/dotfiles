from utils.theme import Colors

start_nm_applet = ["nm-applet"]
set_background = ["xsetroot", "-solid", Colors.BG_SECONDARY] 
launch_application = ["rofi", "-show-icons", "-matching", "fuzzy", "-show", "drun"]
screen_shot = "import png:- | xclip -selection clipboard -t image/png"