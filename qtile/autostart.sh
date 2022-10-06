#!/bin/sh
#nitrogen --set-auto --random "/home/arthurhagen/Pictures/wallpaper/active/" &
/home/arthurhagen/.config/nitrogen/randwallpaper /home/arthurhagen/.config/nitrogen/bg-saved.cfg ~/Pictures/wallpaper/active/ &
nitrogen --restore &
picom &
conky &
