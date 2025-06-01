#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main(void)
{
    const char *msg = "Hello World from user space\n";
    char buf[64] = {0};

    int fd = open("/dev/flash_demo", O_RDWR);
    if (fd < 0) { perror("open"); return 1; }

    write(fd, msg, strlen(msg));
    lseek(fd, 0, SEEK_SET);
    read(fd, buf, sizeof(buf) - 1);
    printf("Reply from kernel: %s", buf);

    close(fd);
    return 0;
}
