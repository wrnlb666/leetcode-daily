#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct {
    size_t  cap;
    size_t  len;
    int     items[];
} CustomStack;


CustomStack* customStackCreate(int maxSize) {
    CustomStack* res = malloc(sizeof (CustomStack) +
                              sizeof (int) * maxSize);
    *res = (CustomStack) {
        .cap    = maxSize,
        .len    = 0,
    };
    memset(res->items, 0, sizeof (int) * maxSize);
    return res;
}

void customStackPush(CustomStack* obj, int x) {
    if (obj->len != obj->cap) {
        obj->items[obj->len] = x;
        obj->len += 1;
    }
}

int customStackPop(CustomStack* obj) {
    if (obj->len != 0) {
        obj->len -= 1;
        return obj->items[obj->len];
    }
    return -1;
}

void customStackIncrement(CustomStack* obj, int k, int val) {
    k = k > obj->len ? obj->len : k;
    for (int i = 0; i < k; i++) {
        obj->items[i] += val;
    }
}

void customStackFree(CustomStack* obj) {
    free(obj);
}

/**
 * Your CustomStack struct will be instantiated and called as such:
 * CustomStack* obj = customStackCreate(maxSize);
 * customStackPush(obj, x);
 
 * int param_2 = customStackPop(obj);
 
 * customStackIncrement(obj, k, val);
 
 * customStackFree(obj);
*/
