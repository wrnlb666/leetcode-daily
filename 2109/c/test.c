#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char* addSpaces(char* s, int* spaces, int spacesSize) {
    int size = strlen(s);
    char* res = malloc(sizeof (char) * (size + spacesSize + 1));

    int index = 0;
    int si = 0;
    for (int i = 0; i < size; i++, index++) {
        if (si < spacesSize && i == spaces[si]) {
            si += 1;
            res[index] = ' ';
            index += 1;
        }
        res[index] = s[i];
    }
    res[index] = 0;
    return res;
}


int main(void) {
    char* s = "LeetcodeHelpsMeLearn";
    int spaces[] = {8,13,15};
    int spacesSize = sizeof (spaces) / sizeof (int);

    char* res = addSpaces(s, spaces, spacesSize);
    printf("%s\n", res);
}
