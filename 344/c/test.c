#include <stdio.h>


void reverseString(char* s, int sSize) {
    for (int i = 0, j = sSize - 1; i < j; (i++, j--)) {
        char tmp = s[i];
        s[i] = s[j];
        s[j] = tmp;
    }
}


int main(void) {
    char s[] = "hello";
    int sSize = sizeof (s) - 1;
    reverseString(s, sSize);
    printf("%s\n", s);
    return 0;
}
