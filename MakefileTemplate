CC = gcc
CFLAG = -Wall -Wextra -std=gnu17 -g -fsanitize=leak,bounds,address

all: test

test: test.c
	@ $(CC) $(CFLAG) $< -o $@

run: all
	@ ./test

clean:
	rm -f test

