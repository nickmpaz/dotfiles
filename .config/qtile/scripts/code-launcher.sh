#!/bin/bash

code_path=~/Code
selection=$(ls $code_path | rofi -dmenu -p "Open" -no-custom)

[[ ! -z "${selection}" ]] && code ${code_path}/${selection}

exit 0
