#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>

/**
  * main - write a string to the stderr
  *
  *Return: Always 0
  */

int main(void)
{
	char *str = "and that piece of art is useful - Dora Korpar, 2015-10-19\n";

	write(2, str, strlen(str));
	exit(EXIT_SUCCESS);
}
