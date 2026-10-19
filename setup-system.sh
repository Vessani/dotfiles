#!/usr/bin/env bash
# System-level setup (needs sudo): packages, ABNT2 keymap, Wi-Fi fixes.
set -euo pipefail

DOTFILES="$(cd "$(dirname "$0")" && pwd)"

echo "==> Installing packages"
grep -v '^#' "$DOTFILES/packages.txt" | sudo pacman -S --needed --noconfirm -

echo "==> Keyboard: ABNT2 on console and X11/Wayland defaults"
sudo localectl set-keymap br-abnt2
sudo localectl set-x11-keymap br abnt2

echo "==> Wi-Fi fixes (NetworkManager powersave + rtw88 options)"
sudo install -Dm644 "$DOTFILES/system/etc/NetworkManager/conf.d/wifi-powersave.conf" \
    /etc/NetworkManager/conf.d/wifi-powersave.conf
sudo install -Dm644 "$DOTFILES/system/etc/modprobe.d/rtw88.conf" \
    /etc/modprobe.d/rtw88.conf
sudo systemctl enable --now NetworkManager
sudo rfkill unblock wifi
nmcli radio wifi on

echo "==> Done. Reboot to apply the rtw88 module options."
