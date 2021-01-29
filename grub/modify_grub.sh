sed -i -e 's/GRUB_TIMEOUT=5/GRUB_TIMEOUT=3\nGRUB_HIDDEN_TIMEOUT_QUIET=false\nGRUB_TIMEOUT_STYLE=countdown/g' /etc/default/grub
update-grub
