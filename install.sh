#!/usr/bin/env bash

sudo apt update
sudo apt upgrade -y
sudo apt install --no-install-recommends -y \
     xserver-xorg-video-intel \
     xorg xdm qiv policykit-1 \
     xmonad libghc-xmonad-contrib-dev xmobar \
     dmenu rofi compton \
     xscreensaver feh \
     network-manager-gnome fdpowermon stalonetray \
     konsole rxvt-unicode-256color neofetch \
     ttf-ubuntu-font-family fonts-font-awesome\
     vim vifm htop pcmanfm \
     rsync patch make stow \
     gimp inkscape scrot okular emacs firefox-esr

sudo mkdir -p /usr/lib/X11/background
mkdir -p $HOME/.config

stow desktop-files
stow profile
stow scripts
stow stalonetray
stow xmobar
stow xmonad
stow xresources
stow xscreensaver
stow xsessionrc

sudo stow xdm

chmod +x $HOME/bin/*.sh

sudo sed -i -e 's/GRUB_TIMEOUT=5/GRUB_TIMEOUT=3\nGRUB_HIDDEN_TIMEOUT_QUIET=false\nGRUB_TIMEOUT_STYLE=countdown/g' /etc/default/grub
sudo update-grub

if grep -Fxq "PS1='\n\[\e[1m\]\[\e[38;2;211;54;130m\]\w\n\[\e[38;2;42;161;152m\]>>> \[\e[0m\]'" $HOME/.bashrc
then
     echo "prompt already in .bashrc"
else
     echo "PS1='\n\[\e[1m\]\[\e[38;2;211;54;130m\]\w\n\[\e[38;2;42;161;152m\]>>> \[\e[0m\]'" >> $HOME/.bashrc
fi

if grep -Fxq "neofetch" $HOME/.bashrc
then
     echo "neofetch already in .bashrc"
else
     echo "neofetch" >> $HOME/.bashrc
fi

# SHUTDOWN WITHOUT SUDO
sudo groupadd wheel
sudo usermod -a -G wheel matthias
sudo visudo
Add Line:: %wheel ALL= NOPASSWD: /sbin/shutdown /sbin/reboot
sudo ln -sf $HOME/bin/shutdown.sh /usr/bin/shutdown.sh
sudo ln -sf $HOME/bin/restart.sh /usr/bin/restart.sh


# MAKE UBUINTU KNOWN TO XSCREENSAVER AND OTHER X-PROGRAMMS
cd /usr/share/fonts/truetype/ubuntu/
sudo mkfontscale
sudo mkfontdir
xset +fp /usr/share/fonts/truetype/ubuntu/
xset fp rehash
xrdb -merge ~/.Xdefaults
