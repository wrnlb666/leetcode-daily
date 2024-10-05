#include <stdio.h>
#include <stdlib.h>
#include <string.h>


bool compare(int c1[26], int c2[26]) {
    for (int i = 0; i < 26; i++) {
        if (c1[i] != c2[i]) {
            return false;
        }
    }
    return true;
}


bool checkInclusion(char* s1, char* s2) {
    int c1[26] = {};
    int c2[26] = {};
    size_t l1 = strlen(s1);
    size_t l2 = strlen(s2);
    if (l2 < l1) {
        return false;
    }

    for (size_t i = 0; i < l1; i++) {
        c1[s1[i] - 'a'] += 1;
    }
    
    for (size_t i = 0; i < l1; i++) {
        c2[s2[i] - 'a'] += 1;
    }

    if (compare(c1, c2) == true) {
        return true;
    }
    for (size_t i = 1; i < l2 - l1 + 1; i++) {
        c2[s2[i - 1] - 'a'] -= 1;
        c2[s2[i + l1 - 1] - 'a'] += 1;
        if (compare(c1, c2) == true) {
            return true;
        }
    }
    return false;
}


int main(void) {
    char* s1 = "ab";
    char* s2 = "eidboaoo";
    bool res = checkInclusion(s1, s2);
    printf("%s\n", res ? "True" : "False");

    return 0;
}
