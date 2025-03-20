from typing import List


class UnionFind:
    parent: List[int]
    depth: List[int]
    _cache: List[int]

    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.depth = [0] * n
        self._cache = [-1] * n

    def _find(self, n: int) -> int:
        if self.parent[n] == n:
            return n
        else:
            return self._find(self.parent[n])

    def find(self, n: int):
        if self._cache[n] != -1:
            return self._cache[n]
        r: int = self._find(n)
        self._cache[n] = r
        return r

    def cmp(self, n1: int, n2: int) -> bool:
        return self.find(n1) == self.find(n2)

    def union(self, n1: int, n2: int) -> None:
        r1: int = self._find(n1)
        r2: int = self._find(n2)
        if r1 == r2:
            return
        if self.depth[r1] < self.depth[r2]:
            r1, r2 = r2, r1
        self.parent[r2] = r1
        if self.depth[r1] == self.depth[r2]:
            self.depth[r1] += 1


class Solution:
    def minimumCost(self, n, edges, queries):
        uf: UnionFind = UnionFind(n)

        costs: List[int] = [-1] * n

        for n1, n2, _ in edges:
            uf.union(n1, n2)

        for n1, n2, w in edges:
            root = uf.find(n1)
            costs[root] &= w

        res: List[int] = list()
        for n1, n2 in queries:
            if not uf.cmp(n1, n2):
                res.append(-1)
            else:
                root = uf.find(n1)
                res.append(costs[root])

        return res


def main() -> None:
    n: int = 5
    edges: List[List[int]] = [[0, 1, 7], [1, 3, 7], [1, 2, 1]]
    query: List[List[int]] = [[0, 3], [3, 4]]
    res: List[int] = Solution().minimumCost(n, edges, query)
    print(res)


if __name__ == "__main__":
    main()
