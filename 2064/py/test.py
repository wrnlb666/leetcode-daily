from typing import List, Tuple
import math
import heapq


class Solution:
    def minimizedMaximum(self, n, quantities):
        m: int = len(quantities)

        cache: List[Tuple[float, int, int]] = [(-q, q, 1) for q in quantities]

        heapq.heapify(cache)

        for _ in range(n - m):
            _, total_quantity, stores_assigned = heapq.heappop(cache)
            new_stores: int = stores_assigned + 1
            weight: float = total_quantity / new_stores
            heapq.heappush(cache, (-weight, total_quantity, new_stores))

        _, total_quantity, stores_assigned = heapq.heappop(cache)

        return math.ceil(total_quantity / stores_assigned)


def main() -> None:
    n: int = 6
    quantities: List[int] = [11,6]

    res: int = Solution().minimizedMaximum(n, quantities)
    print(res)


if __name__ == "__main__":
    main()
