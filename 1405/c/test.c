#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


char* longestDiverseString(int a, int b, int c) {
    // largest size would be `a + b + c + 1`
    char* res = malloc(sizeof (char) * (a + b + c + 1));

    typedef struct {
        int a;
        int b;
        int c;
    } curr_t;
    curr_t curr = {0};

    int i = 0;
    for (;; i++) {
        if (a >= b && a >= c && a > 0) {
            if (curr.a < 2) {
                res[i] = 'a';
                a -= 1;
                curr = (curr_t){.a = curr.a + 1};
            } else {
                if (b >= c && b > 0) {
                    res[i] = 'b';
                    b -= 1;
                    curr = (curr_t){.b = curr.b + 1};
                } else if (c > 0) {
                    res[i] = 'c';
                    c -= 1;
                    curr = (curr_t){.c = curr.c + 1};
                } else {
                    break;
                }
            }
        } else if (b >= a && b >= c && b > 0) {
            if (curr.b < 2) {
                res[i] = 'b';
                b -= 1;
                curr = (curr_t){.b = curr.b + 1};
            } else {
                if (a >= c && a > 0) {
                    res[i] = 'a';
                    a -= 1;
                    curr = (curr_t){.a = curr.a + 1};
                } else if (c > 0) {
                    res[i] = 'c';
                    c -= 1;
                    curr = (curr_t){.c = curr.c + 1};
                } else {
                    break;
                }
            }
        } else if (c >= a && c >= b && c > 0) {
            if (curr.c < 2) {
                res[i] = 'c';
                c -= 1;
                curr = (curr_t){.c = curr.c + 1};
            } else {
                if (a >= b && a > 0) {
                    res[i] = 'a';
                    a -= 1;
                    curr = (curr_t){.a = curr.a + 1};
                } else if (b > 0) {
                    res[i] = 'b';
                    b -= 1;
                    curr = (curr_t){.b = curr.b + 1};
                } else {
                    break;
                }
            }
        } else {
            break;
        }
    }

    res[i] = 0;
    return res;
}


int main(void) {
    int a = 3;
    int b = 0;
    int c = 4;

    char* res = longestDiverseString(a, b, c);
    printf("%s\n", res);
    free(res);

    return 0;
}
