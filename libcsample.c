#include <stdio.h>

void foo(void)
{
    printf("Hello, I am a shared library\n");
}

int add(int a, int b)
{
    return a + b;
}

void hello(char* name)
{
    printf("Hello %s", name);
}


/*
gcc -shared -fPIC -o libcsample.so libcsample.c
*/
