#!/bin/bash

# When restarting Xmonad, the running instanc(es) of Xmobar are not closed,
# This script kills all instances of Xmobar for Xmonad to start a new Xmobar
# with the current config.

for PID in `pgrep xmobar`; do
    kill ${PID} > /dev/null &
done
