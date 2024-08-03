CC = gcc
CFLAG = -std=gnu17 -O2 -g -fsanitize=address,bounds,undefined,leak

all: test

test: test.c
	@ $(CC) $(CFLAG) $< -o $@

run: all
	@ ./test

clean:
	rm -f test

