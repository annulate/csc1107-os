cd flash_demo
sudo ./run_flash_demo.sh
#watch the dmesg as you plug in and unplug your flash drive. You should see flash_demo messages
#When done,
sudo rmmod flash_demo
make clean

