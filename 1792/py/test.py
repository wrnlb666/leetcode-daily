from typing import List, Tuple
import heapq


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        queue: List[Tuple[float, int, int]] = list()
        for s, t in classes:
            heapq.heappush(queue, (s/t - (s+1)/(t+1), s, t))
        for _ in range(extraStudents):
            _, s, t = heapq.heappop(queue)
            heapq.heappush(queue, ((s+1)/(t+1) - (s+2)/(t+2), s+1, t+1))
        res: float = 0.0
        for _, s, t in queue:
            res += s/t
        res /= len(classes)
        return res


def main() -> None:
    classes: List[List[int]] = [[2,4],[3,9],[4,5],[2,10]]
    extraStudents: int = 4
    res: float = Solution().maxAverageRatio(classes, extraStudents)
    print(res)


if __name__ == "__main__":
    main()
