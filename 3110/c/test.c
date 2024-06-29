#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int scoreOfString(char* s) {
    int len = strlen(s);
    int last = s[0];
    int res = 0;
    for (int i = 0; i < len; i++) {
        int curr = s[i];
        res += abs(curr - last);
        last = curr;
    }
    return res;
}


int main(void) {
    char* input = "hello";
    int res = scoreOfString(input);
    printf("%d\n", res);
}
