from re import L
from typing import (
    Tuple,
)
from heapq import (
    heappush,
    heappop,
)

class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        jobs: list[Tuple[int, int]] = sorted(zip(difficulty, profit))
        worker.sort()

        res: int = 0
        maxp: int = 0
        j: int = 0

        for w in worker:
            while j < len(jobs) and jobs[j][0] <= w:
                maxp = max(maxp, jobs[j][1])
                j += 1
            res += maxp

        return res


def main() -> None:
    difficulty: list[int] = [64,88,97]
    profit: list[int] = [53,86,89]
    worker: list[int] = [98,11,6]

    res: int = Solution().maxProfitAssignment(difficulty, profit, worker)
    print(res)


if __name__ == "__main__":
    main()
