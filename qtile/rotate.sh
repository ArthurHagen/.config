#!/bin/sh
#1366x768
current_resolution=xrandr
if ($current_resolution | grep "left (")
then
    xrandr --output eDP-1 --primary --mode 1366x768 --pos 1024x0 --rotate normal --output HDMI-1 --mode $1 --pos 0x168 --rotate inverted
    nitrogen --restore

elif ($current_resolution | grep "inverted (")
then
    xrandr --output eDP-1 --primary --mode 1366x768 --pos 600x256 --rotate normal --output HDMI-1 --mode $1 --pos 0x0 --rotate right
    nitrogen --restore

elif ($current_resolution | grep "right (")
then
    xrandr --output eDP-1 --primary --mode 1366x768 --pos 1024x0 --rotate normal --output HDMI-1 --mode $1 --pos 0x168 --rotate normal
    nitrogen --restore

else
    xrandr --output eDP-1 --primary --mode 1366x768 --pos 600x256 --rotate normal --output HDMI-1 --mode $1 --pos 0x0 --rotate left
    nitrogen --restore
fi
