from typing import List, Tuple
import heapq


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap: List[Tuple[int, int, int]] = [
            (nums[i] * 100 + i, nums[i], i) 
            for i in range(len(nums))
        ]
        heapq.heapify(heap)
        for _ in range(k):
            _, v, i = heapq.heappop(heap)
            v *= multiplier
            heapq.heappush(heap, (v * 100 + i, v, i))
        for (_, v, i) in heap:
            nums[i] = v
        return nums


def main() -> None:
    nums: List[int] = [2,1,3,5,6]
    k: int = 5
    multiplier: int = 2

    res: List[int] = Solution().getFinalState(nums, k, multiplier)
    print(res)


if __name__ == "__main__":
    main()
