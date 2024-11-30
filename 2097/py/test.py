from typing import Deque, List, Dict
from collections import defaultdict, deque


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adj_set: Dict[int, Deque[int]] = defaultdict(deque)
        in_degree: Dict[int, int] = defaultdict(int)
        out_degree: Dict[int, int] = defaultdict(int)

        for (s, e) in pairs:
            adj_set[s].append(e)
            out_degree[s] += 1
            in_degree[e] += 1

        res: List[int] = list()

        def visit(node: int):
            while adj_set[node]:
                next: int = adj_set[node].popleft()
                visit(next)
            res.append(node)

        start = -1
        for node in out_degree:
            if out_degree[node] == in_degree[node] + 1:
                start = node
                break

        if start == -1:
            start = pairs[0][0]

        visit(start)

        res.reverse()

        return [
            [res[i-1], res[i]] 
            for i in range(1, len(res))
        ]


def main() -> None:
    pairs: List[List[int]] = [[1,3],[3,2],[2,1]]
    res: List[List[int]] = Solution().validArrangement(pairs)
    print(res)


if __name__ == "__main__":
    main()
