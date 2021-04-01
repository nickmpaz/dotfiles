import os
from jinja2 import FileSystemLoader, Environment
from themes.material_dark import theme

def generate_themed_config(template, destination):
    templateLoader = FileSystemLoader(searchpath=os.path.expanduser("~/.config/qtile/templates"))
    templateEnv = Environment(loader=templateLoader)
    template = templateEnv.get_template(template)
    outputText = template.stream(theme).dump(destination)

if __name__ == "__main__":
    generate_themed_config("alacritty.yml", os.path.expanduser( "~/.config/alacritty/alacritty.yml" ))