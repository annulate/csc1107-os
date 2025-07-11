/* flash_cli.c
 *
 * Opens /dev/flash_demo, writes a greeting, then reads the kernel reply.
 * Compile with: gcc -Wall -o flash_cli flash_cli.c
 */

#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

#define DEV_PATH  "/dev/flash_demo"

int main(void)
{
        int fd = open(DEV_PATH, O_RDWR);
        if (fd < 0) {
                perror("open");
                return 1;
        }

        const char msg[] = "Hello World from the user space\n";
        if (write(fd, msg, sizeof(msg)) < 0) {
                perror("write");
                return 1;
        }
        printf("Sent to kernel: %s", msg);

        char buf[64] = {0};
        ssize_t r = read(fd, buf, sizeof(buf));
        if (r < 0) {
                perror("read");
                return 1;
        }

        printf("Kernel replied: %s", buf);
        close(fd);
        return 0;
}
