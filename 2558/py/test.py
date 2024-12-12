from typing import List
import math
import heapq


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-n for n in gifts]
        heapq.heapify(gifts)
        for _ in range(k):
            n: int = -heapq.heappop(gifts)
            heapq.heappush(gifts, -math.floor(n ** 0.5))
        return -sum(gifts)


def main() -> None:
    gifts: List[int] = [25,64,9,4,100]
    k: int = 4

    res: int = Solution().pickGifts(gifts, k)
    print(res)


if __name__ == "__main__":
    main()
