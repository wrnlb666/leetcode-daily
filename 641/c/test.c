#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>


typedef struct {
    int     size;
    int     cap;
    int     head;
    int     items[];
} MyCircularDeque;


MyCircularDeque* myCircularDequeCreate(int k) {
    MyCircularDeque* res = malloc(sizeof (MyCircularDeque) + sizeof (int) * k);
    *res = (MyCircularDeque) {
        .size   = 0,
        .cap    = k,
        .head   = 0,
    };
    return res;
}

bool myCircularDequeInsertFront(MyCircularDeque* obj, int value) {
    if (obj->size == obj->cap) {
        return false;
    }
    if (obj->head != 0) {
        obj->head -= 1;
        obj->items[obj->head] = value;
    } else {
        memmove(&obj->items[1], &obj->items[0], sizeof (int) * obj->size);
    }
    obj->size += 1;
    obj->items[obj->head] = value;
    return true;
}

bool myCircularDequeInsertLast(MyCircularDeque* obj, int value) {
    if (obj->size == obj->cap) {
        return false;
    }
    if (obj->head + obj->size >= obj->cap) {
        memmove(&obj->items[0], &obj->items[obj->head], sizeof (int) * obj->size);
        obj->head = 0;
    }
    obj->items[obj->head + obj->size] = value;
    obj->size += 1;
    return true;
}

bool myCircularDequeDeleteFront(MyCircularDeque* obj) {
    if (obj->size > 0) {
        obj->head += 1;
        obj->size -= 1;
        return true;
    }
    return false;
}

bool myCircularDequeDeleteLast(MyCircularDeque* obj) {
    if (obj->size > 0) {
        obj->size -= 1;
        return true;
    }
    return false;
}

int myCircularDequeGetFront(MyCircularDeque* obj) {
    if (obj->size > 0) {
        return obj->items[obj->head];
    }
    return -1;
}

int myCircularDequeGetRear(MyCircularDeque* obj) {
    if (obj->size > 0) {
        return obj->items[obj->head + obj->size -1];
    }
    return -1;
}

bool myCircularDequeIsEmpty(MyCircularDeque* obj) {
    if (obj->size == 0) {
        return true;
    }
    return false;
}

bool myCircularDequeIsFull(MyCircularDeque* obj) {
    if (obj->size == obj->cap) {
        return true;
    }
    return false;
}

void myCircularDequeFree(MyCircularDeque* obj) {
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
