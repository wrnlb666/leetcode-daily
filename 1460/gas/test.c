#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


__attribute__((naked))
int cmp_int(const void *a, const void *b) {
    // return *(int *)a - *(int *)b;
    __asm__ volatile (
        ".intel_syntax noprefix;"
        
        "mov rax, [rdi];"
        "sub rax, [rsi];"
        "ret;"

        ".att_syntax prefix;"
    );
}


__attribute__((naked))
bool canBeEqual(int* target, int targetSize, int* arr, int arrSize) {
    __asm__ volatile (
        ".intel_syntax noprefix;"

        "sub rsp, 20;"
        "mov qword ptr [rbp - 8], rdi;"     // target
        "mov qword ptr [rbp - 16], rdx;"    // arr
        "mov dword ptr [rbp - 20], esi;"    // size
        
        // sort target
        "mov rdx, 4;"
        "lea rcx, qword ptr [rip + cmp_int];"
        "call qsort;"

        // sort arr
        "mov rdi, qword ptr [rbp - 16];"
        "mov esi, dword ptr [rbp - 20];"
        "mov rdx, 4;"
        "lea rcx, qword ptr [rip + cmp_int];"
        "call qsort;"

        // load arrays to registers
        "mov rdi, qword ptr [rbp - 8];"     // target
        "mov rsi, qword ptr [rbp - 16];"    // arr
        "mov edx, dword ptr [rbp - 20];"    // size
        "add rsp, 20;"

        // for loop
        "mov r8d, 0;"                        // int i = 0
        ".loop_start: ;"

        "cmp r8d, edx;"
        "jge .loop_end;"

        "mov eax, dword ptr [rdi];"
        "cmp eax, dword ptr [rsi];"
        "jne .false;"

        "inc r8d;"                          // i++
        "lea rdi, qword ptr [rdi + 4];"     // target++
        "lea rsi, qword ptr [rsi + 4];"     // arr++

        "jmp .loop_start;"
        ".loop_end: ;"
        "mov rax, 1;"
        "ret;"

        ".false: ;"
        "mov rax, 0;"
        "ret;"

        ".att_syntax prefix;"
    );
}


int cmp_int2(const void *a, const void *b) {
    return *(int *)a - *(int *)b;
}


bool canBeEqual2(int* target, int targetSize, int* arr, int arrSize) {
    qsort(target, targetSize, sizeof (int), cmp_int);
    qsort(arr, arrSize, sizeof (int), cmp_int2);

    for (int i = 0; i < targetSize; i++) {
        if (target[i] != arr[i]) {
            return false;
        }
    }
    return true;
}


int main(void) {
    int target[] = {202,401,613,972,423,1000,398,129,35,384,819,537,896,725,138,6,936,259,381,522,168,476,994,639,661,308,895,429,748,504,528,456,938,949,725,675,546,604,852,809,288,933,530,827,923,413,762,890,222,994,281,435,917,369,225,948,806,891,577,378,477,776,722,173,434,782,171,101,873,58,226,285,161,767,580,517,303,928,146,915,738,391,325,341,693,993,639,279,408,179,674,811,965,389,392,312,647,619,851,589,203,472,760,29,175,228,929,332,460,616,710,461,977,800,372,733,843,377,350,39,398,22,789,192,79,479,44,476,392,230,800,83,391,466,808,39,763,492,846,518,854,926,281,732,556,850,715,467,660,69,632,115,832,812,781,37,942,481,226,536,823,259,236,15,620,967,230,247,349,618,715,627,280,15,803,993,675,620,248,319,717,442,689,585,501,10,511,711,842,216,61,193,135,917,796,55,212,1,342,651,693,778,667,51,785,895,369,146,649,301,505,94,599,399,63,872,708,633,343,484,578,430,109,289,232,108,905,696,228,211,280,749,590,937,140,4,510,402,686,591,988,398,269,185,880,683,296,567,686,60,63,539,808,27,558,361,99,848,216,207,391,695,681};
    int targetSize = sizeof (target) / sizeof (int);
    int arr[] = {59,489,29,53,208,933,366,806,300,524,782,400,521,692,183,204,181,259,939,541,330,654,797,315,917,220,896,23,804,518,274,259,637,715,102,662,720,311,118,680,807,21,128,187,849,857,761,208,599,642,591,99,993,17,61,145,836,351,678,603,379,716,946,47,413,561,702,935,545,709,475,937,396,352,834,542,425,852,163,356,555,6,109,464,309,731,936,638,600,114,325,740,109,17,701,678,401,314,608,424,430,319,811,840,724,200,901,753,761,854,261,485,417,279,981,842,56,158,417,727,434,20,504,836,78,693,797,260,849,746,625,14,420,434,406,212,8,670,729,478,121,180,912,369,972,307,706,749,987,758,507,473,1,840,198,113,249,731,536,959,68,841,201,818,649,909,7,212,186,831,906,690,752,694,910,169,942,437,151,868,316,334,726,453,132,377,350,735,297,600,538,875,38,943,641,881,481,489,469,764,717,891,995,665,782,937,821,254,26,581,161,984,807,750,288,966,132,474,337,769,503,495,64,859,997,107,857,80,689,862,375,442,20,802,952,631,100,91,765,638,293,475,418,263,999,135,337,653,387,682,354,59,266,304,483,344,754,852,575,247,853,923,754};
    int arrSize = sizeof (arr) / sizeof (int);

    bool res = canBeEqual(target, targetSize, arr, arrSize);
    printf("%s\n", res ? "true" : "false");
    return 0;
}
