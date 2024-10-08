#include <stdio.h>


int minSwaps(char* s) {
    int stack_size = 0;

    for (char* c = s; *c != '\0'; c++) {
        if (*c == '[') {
            stack_size += 1;
        } else {
            if (stack_size > 0) {
                stack_size -= 1;
            }
        }
    }

    return (stack_size + 1) / 2;
}


int main(void) {
    auto s = "]]][[[";
    auto res = minSwaps(s);
    printf("%d\n", res);

    return 0;
}
