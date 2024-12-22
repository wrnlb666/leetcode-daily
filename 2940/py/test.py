from typing import List, Tuple
import heapq


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        table: List[Tuple[int, int]] = list()
        res: List[int] = [-1] * len(queries)
        cache: List[List[Tuple[int, int]]] = [list() for _ in heights]

        for i, (a, b) in enumerate(queries):
            if a < b and heights[a] < heights[b]:
                res[i] = b
            elif a > b and heights[a] > heights[b]:
                res[i] = a
            elif a == b:
                res[i] = a
            else:
                cache[max(a, b)].append((max(heights[a], heights[b]), i))

        for i, height in enumerate(heights):
            while table and table[0][0] < height:
                _, q = heapq.heappop(table)
                res[q] = i
            for element in cache[i]:
                heapq.heappush(table, element)

        return res


def main() -> None:
    heights: List[int] = [6,4,8,5,2,7]
    queries: List[List[int]] = [[0,1],[0,3],[2,4],[3,4],[2,2]]
    res: List[int] = Solution().leftmostBuildingQueries(heights, queries)
    print(res)


if __name__ == "__main__":
    main()
