CC = gcc
CFLAG = -Wall -Wextra -std=gnu2x -g

all: test

test: test.c
	@ $(CC) $(CFLAG) $< -o $@

run: all
	@- ./test

clean: 
	rm test


