/*
 * main.c : Defines the entry point for the console application.
 */

#include <stdio.h>
#include <string.h>
#include "lwpkt/lwpkt.h"

extern int example_lwpkt(void);
extern int example_lwpkt_evt(void);
extern int test_lwpkt(void);

int
main() {
    return test_lwpkt();
}
