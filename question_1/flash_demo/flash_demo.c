/* flash_demo.c  –  kernel ↔ user demo for Raspberry Pi USB hot-plug
 *
 * Features
 *   • Logs USB add/remove events.
 *   • Misc character device /dev/flash_demo :
 *       - write()  echoes user string into dmesg.
 *       - read()   returns “Hello World from the kernel space” and
 *                  logs that reply to dmesg.
 *   • GPL-licensed, single source file, heavily commented for clarity.
 */

#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>        /* pr_info(), etc.                       */
#include <linux/miscdevice.h>
#include <linux/fs.h>            /* struct file_operations                */
#include <linux/uaccess.h>       /* copy_to_user / copy_from_user         */
#include <linux/usb.h>           /* notifier for USB hot-plug             */

#define DRV_NAME   "flash_demo"
#define KBUF_SIZE  128           /* buffer for user -> kernel message     */

static char kbuf[KBUF_SIZE];     /* last string written from user space   */

/* -------------------------------------------------------------------- */
/*  read() – returns a fixed greeting once per open() and logs reply     */

static ssize_t flash_read(struct file *filp, char __user *ubuf,
                          size_t len, loff_t *ppos)
{
        const char reply[] = "Hello World from the kernel space\n";
        size_t rlen = sizeof(reply);

        if (*ppos)                       /* already read once → EOF        */
                return 0;

        if (len < rlen)                  /* user buffer too small          */
                return -EINVAL;

        if (copy_to_user(ubuf, reply, rlen))
                return -EFAULT;

        pr_info("[%s] kernel replied: %s", DRV_NAME, reply);  /* NEW LOG */

        *ppos += rlen;
        return rlen;
}

/* -------------------------------------------------------------------- */
/*  write() – copy string from user and log it                           */

static ssize_t flash_write(struct file *filp, const char __user *ubuf,
                           size_t len, loff_t *ppos)
{
        size_t cpylen = len < (KBUF_SIZE - 1) ? len : (KBUF_SIZE - 1);

        if (copy_from_user(kbuf, ubuf, cpylen))
                return -EFAULT;

        kbuf[cpylen] = '\0';
        pr_info("[%s] user wrote: %s", DRV_NAME, kbuf);

        return len;                      /* report all bytes “consumed”    */
}

/* -------------------------------------------------------------------- */
/*  file-ops table                                                       */

static const struct file_operations flash_fops = {
        .owner  = THIS_MODULE,
        .read   = flash_read,
        .write  = flash_write,
};

/* -------------------------------------------------------------------- */
/*  misc device registration                                             */

static struct miscdevice flash_dev = {
        .minor = MISC_DYNAMIC_MINOR,
        .name  = DRV_NAME,
        .fops  = &flash_fops,
        .mode  = 0666               /* world R/W for easy testing         */
};

/* -------------------------------------------------------------------- */
/*  USB hot-plug notifier                                                */

static int flash_usb_cb(struct notifier_block *nb,
                        unsigned long action, void *data)
{
        if (action == USB_DEVICE_ADD)
                pr_info("[%s] USB device plugged in", DRV_NAME);
        else if (action == USB_DEVICE_REMOVE)
                pr_info("[%s] USB device removed", DRV_NAME);

        return NOTIFY_OK;
}

static struct notifier_block flash_nb = {
        .notifier_call = flash_usb_cb,
};

/* -------------------------------------------------------------------- */
/*  module init / exit                                                   */

static int __init flash_init(void)
{
        int ret;

        ret = misc_register(&flash_dev);
        if (ret) {
                pr_err("[%s] misc_register failed: %d", DRV_NAME, ret);
                return ret;
        }

        usb_register_notify(&flash_nb);
        pr_info("[%s] loaded – device /dev/%s ready", DRV_NAME, DRV_NAME);
        return 0;
}

static void __exit flash_exit(void)
{
        usb_unregister_notify(&flash_nb);
        misc_deregister(&flash_dev);
        pr_info("[%s] unloaded", DRV_NAME);
}

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Your Name <you@example.com>");
MODULE_DESCRIPTION("Kernel/user USB demo – CSC1107");
MODULE_VERSION("1.2");

module_init(flash_init);
module_exit(flash_exit);
