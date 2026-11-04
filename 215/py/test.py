import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        pq: list[int] = []
        for n in nums:
            if len(pq) < k:
                heapq.heappush(pq, n)
            elif pq[0] < n:
                heapq.heappop(pq)
                heapq.heappush(pq, n)

        return pq[0]


nums = [3, 2, 1, 5, 6, 4]
k = 2
print(Solution().findKthLargest(nums, k))
