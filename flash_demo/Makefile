obj-m := flash_demo.o

KDIR ?= /lib/modules/$(shell uname -r)/build
PWD  := $(shell pwd)

all: flash_demo.ko flash_helper

flash_demo.ko:
	$(MAKE) -C $(KDIR) M=$(PWD) modules

flash_helper: flash_helper.c
	$(CC) flash_helper.c -o flash_helper

clean:
	$(MAKE) -C $(KDIR) M=$(PWD) clean
	rm -f flash_helper
