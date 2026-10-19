#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

# Start Hyprland automatically after logging in on tty1
# (other ttys stay plain shells, useful for recovery)
if [[ -z $WAYLAND_DISPLAY && $XDG_VTNR -eq 1 ]]; then
    exec start-hyprland
fi
