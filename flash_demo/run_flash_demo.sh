#!/bin/bash
# A one-click tester for flash_demo.
set -e

# 1. Build everything
make

# 2. Load the module
sudo insmod flash_demo.ko

# 3. Run the user program (writes then reads)
./flash_cli

# 4. Show the last few kernel messages
echo "---- dmesg tail ----"
dmesg | tail -n 15

# 5 Read hot plugs
read -rp "Plug in your USB flash drive now, then press Enter to continue-----------------"
echo "---- new dmesg tail ----"
dmesg | tail -n 15
# 5. Unload and clean
sudo rmmod flash_demo
make clean
