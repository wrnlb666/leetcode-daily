import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        pool: dict[int, int] = Counter()
        for n in nums:
            pool[n] += 1

        pq: list[tuple[int, int]] = []
        for val, cnt in pool.items():
            if len(pq) < k:
                heapq.heappush(pq, (cnt, val))
            elif cnt > pq[0][0]:
                heapq.heappop(pq)
                heapq.heappush(pq, (cnt, val))

        return [val for _, val in pq]


nums = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
k = 2
print(Solution().topKFrequent(nums, k))
