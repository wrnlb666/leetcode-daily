class Solution {
    int regionsBySlashes(List<String> grid) {
        int n = grid.length;
        UnionFind uf = UnionFind(n);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int id = uf.id(i, j);
                if (grid[i][j] == ' ') {
                    // join itself
                    uf.join(uf.up(id), uf.right(id));
                    uf.join(uf.up(id), uf.down(id));
                    uf.join(uf.up(id), uf.left(id));
                } else if (grid[i][j] == '/') {
                    // join itself
                    uf.join(uf.up(id), uf.left(id));
                    uf.join(uf.right(id), uf.down(id));
                } else if (grid[i][j] == '\\') {
                    // join itself
                    uf.join(uf.up(id), uf.right(id));
                    uf.join(uf.left(id), uf.down(id));
                } else {
                    // error
                }
                // join outside
                // join up
                if (i > 0) {
                    uf.join(uf.down(uf.id(i - 1, j)), uf.up(id));
                }
                // join left
                if (j > 0) {
                    uf.join(uf.right(uf.id(i, j - 1)), uf.left(id));
                }
            }
        }
        return uf.region;
    }
}


class UnionFind {
    List<int> parent = [];
    int n = 0;
    int region = 0;

    UnionFind(this.n) {
        int size = n * n * 4;
        parent = List.filled(size, -1);
        region = size;
    }

    int id(int i, int j) {
        return (i * n + j) * 4;
    }

    int up(int n) {
        return n;
    }

    int right(int n) {
        return n + 1;
    }

    int down(int n) {
        return n + 2;
    }

    int left(int n) {
        return n + 3;
    }

    int find(int n) {
        if (parent[n] == -1) {
            return n;
        }
        parent[n] = find(parent[n]);
        return parent[n];
    }

    bool join(int n1, int n2) {
        int p1 = find(n1);
        int p2 = find(n2);
        if (p1 == p2) {
            return true;
        }
        parent[p2] = p1;
        region--;
        return false;
    }

    bool connected(int n1, int n2) {
        int p1 = find(n1);
        int p2 = find(n2);
        return p1 == p2;
    }
}
