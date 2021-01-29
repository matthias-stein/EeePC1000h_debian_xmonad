=====================================
iOTA360 - Debian 10 (Buster) / Xmonad
=====================================

Base Debian System
==================

I first tried to use the (multiarch ISO)[https://cdimage.debian.org/debian-cd/current/multi-arch/iso-cd/]. With that ISO the WiFi card was not recognized, and I had to use my mobile in USB teethering mode, as the iOTA does not have a LAN port. After installation, though, I only got a blank screen after booting. Googling indicated that this would be due to missing, non-free software.

Next, I downloaded [the non-free multiarch ISO](https://cdimage.debian.org/cdimage/unofficial/non-free/cd-including-firmware/current/multi-arch/iso-cd/), which apparently includes the missing firmware. With that ISO even the WiFi card was directly recognized and I was able to use it during the installation.

I created the bootable USB drive using the *Startup Disk Creator* on Ubuntu Gnome. I used the graphical installer to go though the setup. When the installer asked for the "Select and install software" I deselected everything except *Sandard System Utilities*.

root:secret
matthias:matthias

First Boot
==========

The first boot after the base installation, after unlocking, I was in a shell.

WiFi Connection
---------------

First thing to do was to setup a WiFi connection; I mainly followed the [Debian website](https://wiki.debian.org/WiFi/HowToUse#Command_Line). First, the WiFi device needs to be identified:

.. code:: bash
    user?> su
    root?> ip a

This provided me with the name of my WiFi card, which in is ``wlan0``. The card was brought up:

.. code:: bash
    root?> ip link set wlan0 up

Next I scanned for available WLANs:

.. code:: bash
    root?> sudo iwlist wlan0 scan | grep ESSID

Now edit /etc/network/interfaces. The required configuration is much dependent on your particular setup. The following example will work for most commonly found WPA/WPA2 networks:

.. code:: bash
    # my wifi device
    jallow-hotplug wlp2s0
    iface wlp2s0 inet dhcp
        wpa-ssid ESSID
        wpa-psk PASSWORD
        # needed for a hidden network SSID:
        wpa-scan-ssid 1

Bring up your interface and verify the connection:


# ifup wlp2s0
# iw wlp2s0 link
# ip a
    root?> su user
    user?>


Install Programms
-----------------

The only program I install manually is ``git``, everthing else is part of the git repository's ``install.sh`` I clone.


Suckless ST - Simple Terminal
-----------------------------

I manually installed [ST - Simple Terminal](https://st.suckless.org/) by downloading the .tar.gz from the link. Before running

.. code:: bash
    ?> sudo make clean install

in that directory, I patched ST with the following patches:

+   alpha
+   clipboard
+   scrollback
+   no-bold-colors
+   solarized-dark

by running:

.. code:: bash
    ?> patch -p1 < patch_file.diff

which worked for all patches except the solarized color package. The lines from that .diff I copied over manually to replace the color setting in the default ´´config.def.h´´.

The above described build is part of the git repository and gets installed by ``install.sh``.


Wallpaper
=========

The logo in the wallpaper was taken from [the Debian page](https://www.debian.org/logos/index.de.html). I changed the colors to those from the [Solarized theme](https://ethanschoonover.com/solarized/), made a radial background of greys, and put a *Cutout Glow* effect on the logo.
