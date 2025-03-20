#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int* parent;
    int* depth;
    int* cache;
} UnionFind;

static inline UnionFind uf_init(int n) {
    int*      buf = malloc(sizeof(int) * n * 3);
    UnionFind uf = (UnionFind){
        .parent = buf,
        .depth = buf + n,
        .cache = buf + n * 2,
    };
    for (int i = 0; i < n; i++) {
        uf.parent[i] = i;
    }
    memset(uf.depth, 0, sizeof(int) * n);
    memset(uf.cache, -1, sizeof(int) * n);
    return uf;
}

static inline void uf_deinit(UnionFind uf) {
    free(uf.parent);
}

static inline int uf_find(UnionFind uf, int n) {
    if (uf.parent[n] == n) {
        return n;
    }
    return uf_find(uf, uf.parent[n]);
}

static inline int uf_seek(UnionFind uf, int n) {
    if (uf.cache[n] != -1) {
        return uf.cache[n];
    }
    uf.cache[n] = uf_find(uf, n);
    return uf.cache[n];
}

static inline bool uf_cmp(UnionFind uf, int n1, int n2) {
    return uf_seek(uf, n1) == uf_seek(uf, n2);
}

static inline void uf_union(UnionFind uf, int n1, int n2) {
    int r1 = uf_find(uf, n1);
    int r2 = uf_find(uf, n2);
    if (r1 == r2) {
        return;
    }
    if (uf.depth[r1] < uf.depth[r2]) {
        int tmp = r1;
        r1 = r2;
        r2 = tmp;
    }
    uf.parent[r2] = r1;
    if (uf.depth[r1] == uf.depth[r2]) {
        uf.depth[r1] += 1;
    }
}

int* minimumCost(int n, int** edges, int edgesSize, int* edgesColSize, int** query, int querySize, int* queryColSize, int* returnSize) {
    (void)edgesColSize;
    (void)queryColSize;

    UnionFind uf = uf_init(n);
    int*      costs = malloc(sizeof(int) * n);
    memset(costs, -1, sizeof(int) * n);

    for (int i = 0; i < edgesSize; i++) {
        int n1 = edges[i][0];
        int n2 = edges[i][1];
        uf_union(uf, n1, n2);
    }

    for (int i = 0; i < edgesSize; i++) {
        int n1 = edges[i][0];
        int r1 = uf_seek(uf, n1);
        int w = edges[i][2];
        costs[r1] &= w;
    }

    *returnSize = querySize;
    int* res = malloc(sizeof(int) * querySize);
    for (int i = 0; i < querySize; i++) {
        int n1 = query[i][0];
        int n2 = query[i][1];
        if (!uf_cmp(uf, n1, n2)) {
            res[i] = -1;
        } else {
            int root = uf_seek(uf, n1);
            res[i] = costs[root];
        }
    }
    free(costs);
    uf_deinit(uf);
    return res;
}

int main(void) {
    int  n = 5;
    int* edges[3] = {(int[]){0, 1, 7}, (int[]){1, 3, 7}, (int[]){1, 2, 1}};
    int* query[2] = {(int[]){0, 3}, (int[]){3, 4}};
    int  edgesSize = sizeof(edges) / sizeof(int*);
    int  edgesColSize = 3;
    int  querySize = sizeof(query) / sizeof(int*);
    int  queryColSize = 2;
    int  returnSize = -2;

    int* res = minimumCost(n, edges, edgesSize, &edgesColSize, query, querySize, &queryColSize, &returnSize);
    printf("[");
    for (int i = 0; i < returnSize; i++) {
        printf("%3d", res[i]);
    }
    printf("]\n");
    free(res);
}
