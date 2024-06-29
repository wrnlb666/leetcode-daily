#include <stdio.h>
#include <string.h>


int appendCharacters(char* s, char* t) {
    int lens = strlen(s);
    int lent = strlen(t);

    int i = 0;
    int j = 0;

    while (i < lens && j < lent) {
        if (s[i] == t[j]) {
            i++;
            j++;
        } else {
            i++;
        }
    }

    return lent - j;
}


int main(void) {
    char s[] = "vrykt";
    char t[] = "rkge";

    auto res = appendCharacters(s, t);
    printf("%d\n", res);
    return 0;
}
