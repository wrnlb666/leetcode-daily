#include <stdio.h>
#include <stdlib.h>


// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};
struct ListNode* node_init(int);


struct ListNode* from_arr(size_t n, int arr[n]) {
    struct ListNode* head = node_init(arr[0]);
    struct ListNode* node = head;
    for (size_t i = 1; i < n; i++) {
        node->next = node_init(arr[i]);
        node = node->next;
    }
    return head;
}


void print_list(struct ListNode* head) {
    for (struct ListNode* p = head; p != NULL; p = p->next) {
        printf("%3d ", p->val);
    }
    printf("\n");
}


struct ListNode* node_init(int n) {
    struct ListNode* res = malloc(sizeof (struct ListNode));
    res->val = n;
    res->next = NULL;
    return res;
}


int gcd(int a, int b) {
    int c = a % b;
    if (c == 0) {
        return b;
    }
    return gcd(b, c);
}


struct ListNode* insertGreatestCommonDivisors(struct ListNode* head) {
    struct ListNode* prev = head;
    struct ListNode* curr = head->next;
    while (curr != NULL) {
        int a = prev->val;
        int b = curr->val;
        int c = gcd(a, b);
        struct ListNode* mid = node_init(c);
        prev->next = mid;
        mid->next = curr;
        prev = curr;
        curr = curr->next;
    }
    return head;
}


int main(void) {
    int head[] = {18,6,10,3};
    size_t size = sizeof (head) / sizeof (int);
    struct ListNode* res = insertGreatestCommonDivisors(from_arr(size, head));
    print_list(res);

    return 0;
}
