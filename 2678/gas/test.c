#include <stdio.h>


int countSeniors2(char ** details, int detailsSize) {
    int res = 0;
    for (int i = 0; i < detailsSize; i++) {
        char* age_s = &details[i][11];
        int age_i = (age_s[0] - 0x30) * 10 + (age_s[1] - 0x30);
        printf("%d\n", age_i);
        if (age_i > 60) {
            res += 1;
        }
    }
    return res;
}


__attribute__((naked))
int countSeniors(char ** details, int detailsSize) {
    __asm__ volatile (
        ".intel_syntax noprefix;"

        // rdi: details
        // rsi: detailsSize

        // res = 0
        "mov rax, 0;"

        // for loop
        // int i = 0;
        "mov r8, 0;"

        // i < detailsSize
        ".start_loop: ;"
        "cmp r8, rsi;"
        "jge .end_loop;"

        // get string
        "mov r9, [rdi];"

        // get age
        "movzx r10, byte ptr [r9 + 11];"
        "lea r10, [r10] - 0x30;"
        "imul r10, 10;"
        "movzx r11, byte ptr [r9 + 12];"
        "lea r11, [r11] - 0x30;"
        "add r10, r11;"

        // if (age > 60)
        "cmp r10, 60;"
        "jle .end_if;"
        "add rax, 1;"
        ".end_if: ;"

        // details = &details[i]
        "lea rdi, [rdi + 8];"

        // i++
        "inc r8;"
        "jmp .start_loop;"
        ".end_loop: ;"

        "ret;"

        ".att_syntax prefix\n"
    );
}


int main(void) {
    char* details[] = {"9751302862F0693","3888560693F7262","5485983835F0649","2580974299F6042","9976672161M6561","0234451011F8013","4294552179O6482"};
    int detailsSize = sizeof (details) / sizeof (char*);
    int res = countSeniors(details, detailsSize);
    printf("%d\n", res);

    return 0;
}
