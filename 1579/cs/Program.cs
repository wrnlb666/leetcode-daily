int n = 4;
int[][] edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]];
int res = new Solution().MaxNumEdgesToRemove(n, edges);
Console.WriteLine(res);


public class Solution {
    public int MaxNumEdgesToRemove(int n, int[][] edges) {
        UnionFind Alice = new(n);
        UnionFind Bob = new(n);

        int used = 0;
        foreach (int[] edge in edges) {
            bool added = false;
            if (edge[0] == 3) {
                if (Alice.Union(edge[1]-1, edge[2]-1)) {
                    Console.WriteLine(string.Join(" ", edge));
                    used += 1;
                    added = true;
                }
                if (Bob.Union(edge[1]-1, edge[2]-1)) {
                    if (added == false) {
                        Console.WriteLine(string.Join(" ", edge));
                        used += 1;
                    }
                }
                if (Alice.GroupCount() == 1 && Bob.GroupCount() == 1) {
                    return edges.Length - used;
                }
            }
        }
        foreach (int[] edge in edges) {
            if (edge[0] == 1) {
                if (Alice.Union(edge[1]-1, edge[2]-1)) {
                    Console.WriteLine(string.Join(" ", edge));
                    used += 1;
                }
                if (Alice.GroupCount() == 1 && Bob.GroupCount() == 1) {
                    return edges.Length - used;
                }
            }
            if (edge[0] == 2) {
                if (Bob.Union(edge[1]-1, edge[2]-1)) {
                    Console.WriteLine(string.Join(" ", edge));
                    used += 1;
                }
                if (Alice.GroupCount() == 1 && Bob.GroupCount() == 1) {
                    return edges.Length - used;
                }
            }
        }
        return -1;
    }
}

class UnionFind {
    int[]?  data;
    int     groupCount;

    public UnionFind(int n) {
        data = new int[n];
        groupCount = n;
        for (int i = 0; i < n; i++) {
            data[i] = i;
        }
    }

    public int Find(int x) {
        if (data![x] != x) {
            data[x] = Find(data[x]);
        }
        return data[x];
    }

    public bool Union(int x, int y) {
        int rootX = Find(x);
        int rootY = Find(y);
        if (rootX != rootY) {
            data![rootX] = rootY;
            groupCount -= 1;
            return true;
        }
        return false;
    }

    public int GroupCount() {
        return groupCount;
    }
}
