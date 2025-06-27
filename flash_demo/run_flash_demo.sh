#!/usr/bin/env bash

set -e
echo "[*] Building..."
make -s

echo "[*] Inserting kernel module..."
sudo insmod flash_demo.ko || { echo "Module already loaded"; }

./flash_helper                            
echo "Now plug in a USB stick to see the notifier messages in dmesg:"
watch -n0.5 "dmesg | tail -n 30"
