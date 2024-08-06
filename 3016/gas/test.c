#include <stdio.h>
#include <stdlib.h>


__attribute__((naked))
int cmp_int(const void* arg1, const void* arg2) {
    __asm__ volatile (
        ".intel_syntax noprefix;"

        "mov eax, dword ptr [rsi];"
        "sub eax, dword ptr [rdi];"
        "ret;"

        ".att_syntax prefix;"
    );
}


__attribute__((naked))
int minimumPushes(char* word) {
    __asm__ volatile (
        ".intel_syntax noprefix;"

        "sub rsp, 104;"         // count

        // zero initialize frequency
        "push rdi;"
        "lea rdi, [rbp - 104];"
        "mov rsi, 0;"
        "mov rdx, 104;"
        "call memset;"
        "pop rdi;"

        // for loop
        "mov r8, 0;"
        ".count_loop_start: ;"
        "cmp byte ptr [rdi], 0;"
        "je .count_loop_end;"

        "lea rcx, [rbp - 104];"
        "mov r8b, byte ptr [rdi];"
        "lea rcx, [rcx + (r8 - 0x61) * 4];"
        "add dword ptr [rcx], 1;"


        "lea rdi, [rdi + 1];"
        "jmp .count_loop_start;"
        ".count_loop_end: ;"


        // sort count by frequency
        "lea rdi, [rbp - 104];"
        "mov rsi, 26;"
        "mov rdx, 4;"
        "lea rcx, [rip + cmp_int];"
        "call qsort;"


        // for loop calculate
        "mov r10, 0;"
        "lea r8, qword ptr [rbp - 104];"
        "mov r9d, 0;"

        ".calculate_loop_start: ;"
        "cmp r9d, 26;"
        "jge .calculate_loop_end;"

        // if count[i] == 0
        "cmp dword ptr [r8], 0;"
        "je .calculate_loop_end;"

        // res += count[i] * ((i / 8) + 1);
        "mov eax, r9d;"
        "cdq;"
        "mov ecx, 8;"
        "idiv ecx;"
        "inc eax;"
        "mov ecx, dword ptr [r8];"
        "imul ecx;"
        "add r10d, eax;"

        "inc r9d;"
        "lea r8, [r8 + 4];"
        "jmp .calculate_loop_start;"
        ".calculate_loop_end: ;"

        "add rsp, 104;"
        "mov rax, r10;"
        "ret;"
        ".att_syntax prefix;"
    );
}


int cmp_int2(const void* arg1, const void* arg2) {
    return *(int*)arg2 - *(int*)arg1;
}


int minimumPushes2(char* word) {
    // count frequency
    int count[26] = {0};
    for (char* c = word; *c != 0; c++) {
        count[*c - 0x61]++;
    }

    // sort by frequency
    qsort(count, 26, sizeof (int), cmp_int);

    // calculate
    int res = 0;
    for (int i = 0; i < 26; i++) {
        if (count[i] == 0) {
            break;
        }
        res += count[i] * ((i / 8) + 1);
    }

    return res;
}


int main(void) {
    char* word = "xyzxyzxyzxyz";
    int res = minimumPushes(word);
    printf("%d\n", res);

    return 0;
}
