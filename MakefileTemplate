CC = gcc
CFLAG = -Wall -Wextra -std=c2x -g -fsanitize=leak,bounds,address,undefined

all: test

test: test.c
	@ $(CC) $(CFLAG) $< -o $@

run: all
	@ ./test

clean:
	rm -f test

