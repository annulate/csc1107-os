#
# run_flash_demo.sh
# One-step tester for flash_demo:
#   1) build kernel module and CLI
#   2) load module
#   3) wait until a USB device is plugged in
#   4) run flash_cli (write → read)
#   5) show recent dmesg lines
#   6) unload module and clean
#
set -e                      # exit on first error
cd "$(dirname "$0")"        # script directory = flash_demo

# -------- 1. build --------
make

# -------- 2. load module --------
sudo insmod flash_demo.ko

# -------- 3. wait for USB plug --------
echo "Insert the USB flash drive now..."
# Block until flash_demo notifier prints its 'USB device plugged in' line.
sudo dmesg --follow --level=info | while read -r line; do
    if [[ "$line" == *"[flash_demo] USB device plugged in"* ]]; then
        break                # pattern found – stop waiting
    fi
done

# -------- 4. run CLI (write + read) --------
./flash_cli

# -------- 5. show kernel log snippet --------
echo "---- flash_demo messages (last 10) ----"
dmesg | grep -E '\[flash_demo\]' | tail -n 10
# -------- 6. unload and clean --------
sudo rmmod flash_demo
make clean
