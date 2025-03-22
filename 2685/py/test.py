from typing import List, Dict
from collections import Counter


class UnionFind:
    parent: List[int]
    size: List[int]
    _cache: List[int]

    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n
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
        if self.size[r1] > self.size[r2]:
            r1, r2 = r2, r1
        self.parent[r1] = r2
        self.size[r2] += self.size[r1]


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf: UnionFind = UnionFind(n)
        for n1, n2 in edges:
            uf.union(n1, n2)
        cache: Dict[int, int] = Counter()
        for n1, _ in edges:
            r1: int = uf.find(n1)
            cache[r1] += 1
        res: int = 0
        for i, v in enumerate(uf.parent):
            if i == v:
                count: int = uf.size[i]
                expected: int = (count * (count - 1)) // 2
                if cache[v] == expected:
                    res += 1
        return res


def main() -> None:
    n: int = 6
    edges: List[List[int]] = [[0, 1], [0, 2], [1, 2], [3, 4]]
    res: int = Solution().countCompleteComponents(n, edges)
    print(res)


if __name__ == "__main__":
    main()
