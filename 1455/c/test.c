#include <stdio.h>
#include <string.h>
#include <stdbool.h>


int isPrefixOfWord(char* sentence, char* searchWord) {
    int curr = 1;
    int index = 0;
    bool skip = false;
    int ssize = strlen(sentence);
    int wsize = strlen(searchWord);

    for (int i = 0; i < ssize; i++) {
        char v = sentence[i];
        if (v == ' ') {
            curr += 1;
            index = 0;
            skip = false;
            continue;
        }
        if (skip) {
            continue;
        }
        if (v != searchWord[index]) {
            skip = true;
            continue;
        }
        if (index == wsize-1) {
            return curr;
        }
        index += 1;
    }
    return -1;
}


int main(void) {
    char* sentence = "i love eating burger";
    char* searchWord = "burg";

    int res = isPrefixOfWord(sentence, searchWord);
    printf("%d\n", res);
    return 0;
}
