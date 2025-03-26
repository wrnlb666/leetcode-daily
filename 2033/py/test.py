from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        cache: List[int] = list()
        res: int = 0

        for row in grid:
            for num in row:
                cache.append(num)

        cache.sort()
        median: int = cache[len(cache) // 2]

        for n in cache:
            if n % x != median % x:
                return -1
            res += abs(median - n) // x

        return res


def main() -> None:
    grid: List[List[int]] = [[2,4],[6,8]]
    x: int = 2
    res: int = Solution().minOperations(grid, x)
    print(res)


if __name__ == "__main__":
    main()
