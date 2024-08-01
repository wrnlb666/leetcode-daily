#include <stdio.h>


int countSeniors(char ** details, int detailsSize) {
    int res = 0;
    for (int i = 0; i < detailsSize; i++) {
        char* age_s = &details[i][11];
        int age_i = (age_s[0] - 0x30) * 10 + (age_s[1] - 0x30);
        if (age_i > 60) {
            res += 1;
        }
    }
    return res;
}


int main(void) {
    char* details[] = {"7868190130M7522","5303914400F9211","9273338290F4010"};
    int detailsSize = sizeof (details) / sizeof (char*);
    int res = countSeniors(details, detailsSize);
    printf("%d\n", res);

    return 0;
}
