#include <stdio.h>


__attribute__((naked))
int minSwaps(int* nums, int numsSize) {
    __asm__ volatile (
        ".intel_syntax noprefix;"

        // [rbp - 4] = res
        // [rbp - 8] = ones

        "sub rsp, 8;"
        "mov [rbp - 4], rsi;"

        
        // count ones
        "xor r8, r8;"
        "xor rax, rax;"

        // for loop
        ".count_ones_loop_start: ;"
        "cmp rax, rsi;"
        "jge .count_ones_loop_end;"
        "add r8d, dword ptr [rdi + (rax * 4)];"
        "inc rax;"
        "jmp .count_ones_loop_start;"
        ".count_ones_loop_end: ;"
        "mov dword ptr [rbp - 8], r8d;"

        // r8 = count
        // r9 = start
        // r10 = end
        "xor r9, r9;"
        "mov r8d, dword ptr [rdi];"
        "xor r10, r10;"

        // for loop
        ".count_res_loop_start: ;"
        "cmp r9, rsi;"
        "jge .count_res_loop_end;"

        // if start != 0
        "cmp r9, 0;"
        "je .endif_eq;"
        "sub r8d, dword ptr [rdi + (r9 - 1) * 4];"
        ".endif_eq: ;"

        // while loop
        ".while_loop_start: ;"
        "mov eax, r10d;"
        "sub eax, r9d;"
        "inc eax;"
        "cmp eax, dword ptr [rbp - 8];"
        "jge .while_loop_end;"

        "inc r10d;"
        "xor rdx, rdx;"
        "mov eax, r10d;"
        "idiv esi;"
        "add r8d, dword ptr [rdi + rdx * 4];"

        "jmp .while_loop_start;"
        ".while_loop_end: ;"

        // compute res
        "xor rax, rax;"
        "mov eax, dword ptr [rbp - 8];"
        "sub eax, r8d;"
        "cmp eax, dword ptr [rbp - 4];"
        "jge .endif_res;"
        "mov dword ptr [rbp - 4], eax;"
        ".endif_res: ;"

        // start++
        "inc r9d;"
        "jmp .count_res_loop_start;"
        ".count_res_loop_end: ;"


        "xor rax, rax;"
        "mov eax, dword ptr [rbp - 4];"
        "add rsp, 8;"
        "ret;"
        ".att_syntax prefix;"
    );
}


int minSwaps2(int* nums, int numsSize) {
    int res = numsSize;
    int ones = 0;
    for (int i = 0; i < numsSize; i++) {
        ones += nums[i];
    }

    int count = nums[0];
    int end = 0;

    for (int start = 0; start < numsSize; start++) {
        if (start != 0) {
            count -= nums[start - 1];
        }

        while (end - start + 1 < ones) {
            end += 1;
            count += nums[end % numsSize];
        }

        res = res < (ones - count) ? res : (ones - count);
    }

    return res;
}


int main(void) {
    int nums[] = {0,1,0,1,1,0,0};
    int numsSize = sizeof (nums) / sizeof (int);

    int res = minSwaps(nums, numsSize);
    printf("%d\n", res);

    return 0;
}
