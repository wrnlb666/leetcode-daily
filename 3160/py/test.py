from typing import List, Dict
from collections import defaultdict


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res: List[int] = list()
        map: Dict[int, int] = defaultdict(int)
        cache: Dict[int, int] = dict()

        for i in range(len(queries)):
            ball, color = queries[i]
            if ball in cache:
                prev = cache[ball]
                map[prev] -= 1
                if map[prev] == 0:
                    del map[prev]

            cache[ball] = color
            map[color] = map[color] + 1
            res.append(len(map))

        return res


def main() -> None:
    limit: int = 4
    queries: List[List[int]] = [[1,4],[2,5],[1,3],[3,4]]
    res: List[int] = Solution().queryResults(limit, queries)
    print(res)


if __name__ == "__main__":
    main()
