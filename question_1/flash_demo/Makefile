# -------- kernel module build variables -------------------------------
KDIR    ?= /lib/modules/$(shell uname -r)/build
PWD     := $(shell pwd)

obj-m   := flash_demo.o

# -------- default target ------------------------------------------------
all: flash_demo.ko flash_cli

# Compile kernel module
flash_demo.ko: flash_demo.c
	$(MAKE) -C $(KDIR) M=$(PWD) modules

# Compile user program
flash_cli: flash_cli.c
	$(CC) -Wall -o $@ $<

# -------- clean target --------------------------------------------------
clean:
	$(MAKE) -C $(KDIR) M=$(PWD) clean
	$(RM) flash_cli

.PHONY: all clean
