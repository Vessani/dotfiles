#!/usr/bin/env bash
# Symlink user dotfiles into $HOME. Existing files are backed up as *.bak.
set -euo pipefail

DOTFILES="$(cd "$(dirname "$0")" && pwd)"

link() {
    local src=$1 dst=$2
    mkdir -p "$(dirname "$dst")"
    if [[ -L $dst ]]; then
        rm "$dst"
    elif [[ -e $dst ]]; then
        mv "$dst" "$dst.bak"
        echo "backup: $dst -> $dst.bak"
    fi
    ln -s "$src" "$dst"
    echo "link:   $dst -> $src"
}

for f in "$DOTFILES"/home/.[!.]*; do
    link "$f" "$HOME/$(basename "$f")"
done

for d in "$DOTFILES"/config/*; do
    link "$d" "$HOME/.config/$(basename "$d")"
done

link "$DOTFILES/wallpapers" "$HOME/Pictures/wallpapers"
