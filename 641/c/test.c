#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>


typedef struct node node;
struct node {
    node*   prev;
    node*   next;
    int     val;
};


typedef struct {
    int     size;
    int     cap;
    node*   head;
    node*   tail;
} MyCircularDeque;


MyCircularDeque* myCircularDequeCreate(int k) {
    MyCircularDeque* res = malloc(sizeof (MyCircularDeque));
    *res = (MyCircularDeque) {
        .size   = 0,
        .cap    = k,
        .head   = NULL,
        .tail   = NULL,
    };
    return res;
}

bool myCircularDequeInsertFront(MyCircularDeque* obj, int value) {
    if (obj->size == obj->cap) {
        return false;
    }
    if (obj->head == NULL) {
        obj->head = obj->tail = malloc(sizeof (node));
        *obj->head = (node) {
            .prev   = NULL,
            .next   = NULL,
            .val    = value,
        };
    } else {
        obj->head->prev = malloc(sizeof (node));
        *obj->head->prev = (node) {
            .prev   = NULL,
            .next   = obj->head,
            .val    = value,
        };
        obj->head = obj->head->prev;
    }
    obj->size += 1;
    return true;
}

bool myCircularDequeInsertLast(MyCircularDeque* obj, int value) {
    if (obj->size == obj->cap) {
        return false;
    }
    if (obj->tail == NULL) {
        obj->head = obj->tail = malloc(sizeof (node));
        *obj->tail = (node) {
            .prev   = NULL,
            .next   = NULL,
            .val    = value,
        };
    } else {
        obj->tail->next = malloc(sizeof (node));
        *obj->tail->next = (node) {
            .prev   = obj->tail,
            .next   = NULL,
            .val    = value,
        };
        obj->tail = obj->tail->next;
    }
    obj->size += 1;
    return true;
}

bool myCircularDequeDeleteFront(MyCircularDeque* obj) {
    if (obj->size == 1) {
        free(obj->head);
        obj->head = obj->tail = NULL;
        obj->size = 0;
        return true;
    }
    if (obj->size > 1) {
        node* temp = obj->head;
        obj->head = obj->head->next;
        obj->head->prev = NULL;
        free(temp);
        obj->size -= 1;
        return true;
    }
    return false;
}

bool myCircularDequeDeleteLast(MyCircularDeque* obj) {
    if (obj->size == 1) {
        free(obj->tail);
        obj->head = obj->tail = NULL;
        obj->size = 0;
        return true;
    }
    if (obj->size > 1) {
        node* temp = obj->tail;
        obj->tail = obj->tail->prev;
        obj->tail->next = NULL;
        free(temp);
        obj->size -= 1;
        return true;
    }
    return false;
}

int myCircularDequeGetFront(MyCircularDeque* obj) {
    if (obj->size > 0) {
        return obj->head->val;
    }
    return -1;
}

int myCircularDequeGetRear(MyCircularDeque* obj) {
    if (obj->size > 0) {
        return obj->tail->val;
    }
    return -1;
}

bool myCircularDequeIsEmpty(MyCircularDeque* obj) {
    return obj->size == 0;
}

bool myCircularDequeIsFull(MyCircularDeque* obj) {
    return obj->size == obj->cap;
}

void myCircularDequeFree(MyCircularDeque* obj) {
    node* n = obj->head;
    while (n != NULL) {
        node* next = n->next;
        free(n);
        n = next;
    }
    free(obj);
}

/**
 * Your MyCircularDeque struct will be instantiated and called as such:
 * MyCircularDeque* obj = myCircularDequeCreate(k);
 * bool param_1 = myCircularDequeInsertFront(obj, value);
 
 * bool param_2 = myCircularDequeInsertLast(obj, value);
 
 * bool param_3 = myCircularDequeDeleteFront(obj);
 
 * bool param_4 = myCircularDequeDeleteLast(obj);
 
 * int param_5 = myCircularDequeGetFront(obj);
 
 * int param_6 = myCircularDequeGetRear(obj);
 
 * bool param_7 = myCircularDequeIsEmpty(obj);
 
 * bool param_8 = myCircularDequeIsFull(obj);
 
 * myCircularDequeFree(obj);
*/


#define pnt_bool(b)     printf("%s\n", b ? "True" : "False")
#define pnt_num(n)      printf("%d\n", n)
#define create(n)       myCircularDequeCreate(n)
#define insert_front(n) pnt_bool(myCircularDequeInsertFront(obj, n))
#define insert_last(n)  pnt_bool(myCircularDequeInsertLast(obj, n))
#define delete_front()  pnt_bool(myCircularDequeDeleteFront(obj))
#define delete_last()   pnt_bool(myCircularDequeDeleteLast(obj))
#define is_empty()      pnt_bool(myCircularDequeIsEmpty(obj))
#define is_full()       pnt_bool(myCircularDequeIsFull(obj))
#define get_front()     pnt_num(myCircularDequeGetFront(obj))
#define get_rear()      pnt_num(myCircularDequeGetRear(obj))
#define deque_free()    myCircularDequeFree(obj)


int main(void) {
    MyCircularDeque* obj = create(3);
    insert_front(8);
    insert_last(8);
    insert_last(2);
    get_front();
    delete_last();
    get_rear();
    insert_front(9);
    delete_front();
    get_rear();
    insert_last(2);
    is_full();
    deque_free();


    return 0;
}
