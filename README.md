# dotfiles

Arch Linux + Hyprland (Lenovo IdeaPad, AMD, RTL8822CE).

```
config/   -> ~/.config/<nome>   (hypr, waybar, fuzzel, kitty)
home/     -> ~/<arquivo>        (.bash_profile, .bashrc)
system/   -> arquivos de /etc, aplicados por setup-system.sh
```

## Instalação em máquina nova

```sh
git clone <url> ~/dotfiles
~/dotfiles/setup-system.sh   # pacotes, teclado ABNT2, correções de Wi-Fi (sudo)
~/dotfiles/install.sh        # symlinks (arquivos existentes viram *.bak)
```

Logar no tty1 inicia o Hyprland automaticamente.

## Atalhos

| Tecla | Ação |
|---|---|
| Super+Q | terminal (kitty) |
| Super+R | launcher (fuzzel) |
| Super+C | fechar janela |
| Super+M | sair do Hyprland |
| Super+1..0 | workspaces |
| Teclas de volume/brilho | wpctl / brightnessctl |

Na barra: clique no áudio abre o `audio` (clique direito muta), clique na rede abre o `wifi`,
clique no bluetooth abre o `bt` (clique direito liga/desliga).

`audio`, `wifi` e `bt` (em `bin/`) também funcionam no terminal, com fzf:
`audio`, `audio vol N|mute|mic`, `wifi`, `wifi on|off|status`, `bt`, `bt scan`, `bt on|off`.
