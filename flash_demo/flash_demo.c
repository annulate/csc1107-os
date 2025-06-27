#include <linux/module.h>
#include <linux/usb.h>
#include <linux/fs.h>
#include <linux/miscdevice.h>
#include <linux/uaccess.h>

#define BUF_LEN 64
static char kernel_buf[BUF_LEN] = "Hello World from kernel space\n";

static ssize_t flash_read(struct file *f, char __user *out, size_t len, loff_t *off)
{
    if (*off > 0) return 0;                    /* EOF after first read             */
    if (len > strlen(kernel_buf)) len = strlen(kernel_buf);
    if (copy_to_user(out, kernel_buf, len)) return -EFAULT;
    *off += len;
    return len;
}

static ssize_t flash_write(struct file *f, const char __user *in, size_t len, loff_t *off)
{
    if (len > BUF_LEN - 1) len = BUF_LEN - 1;
    if (copy_from_user(kernel_buf, in, len)) return -EFAULT;
    kernel_buf[len] = '\0';
    pr_info("[flash_demo] got from user: %s", kernel_buf);
    return len;
}

static const struct file_operations flash_fops = {
    .owner  = THIS_MODULE,
    .read   = flash_read,
    .write  = flash_write,
};

static struct miscdevice flash_dev = {
    .minor = MISC_DYNAMIC_MINOR,
    .name  = "flash_demo",
    .fops  = &flash_fops,
};

static int flash_notify(struct notifier_block *nb, unsigned long action, void *data)
{
    struct usb_device *udev = data;

    const char *drv = udev->dev.driver ? udev->dev.driver->name : "none";
    pr_info("flash_demo: event %lu, dev-class 0x%02x, driver=%s\n",
        action,
        udev->descriptor.bDeviceClass,
        drv);

    switch (action) {
    case USB_DEVICE_ADD:
        pr_info("[flash_demo] ========== USB flash inserted, misc device ready ==========");
        break;
    case USB_DEVICE_REMOVE:
        pr_info("\n\n[flash_demo] ========== USB flash removed ==========\n\n");
        break;
    }
    return NOTIFY_OK;
}

static struct notifier_block flash_nb = { .notifier_call = flash_notify };

static int __init flash_init(void)
{
    int ret;
    ret = misc_register(&flash_dev);
    if (ret) return ret;
    usb_register_notify(&flash_nb);
    pr_info("[flash_demo] loaded");
    return 0;
}

static void __exit flash_exit(void)
{
    usb_unregister_notify(&flash_nb);
    misc_deregister(&flash_dev);
    pr_info("[flash_demo] unloaded");
}

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Your-Name");
MODULE_DESCRIPTION("USB flash hello-world demo");
module_init(flash_init);
module_exit(flash_exit);
