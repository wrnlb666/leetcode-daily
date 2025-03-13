from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        left, right = 0, len(queries)

        if not self._valid(nums, queries, right):
            return -1

        while left <= right:
            middle = left + (right - left) // 2
            if self._valid(nums, queries, middle):
                right = middle - 1
            else:
                left = middle + 1

        return left

    def _valid(self, nums: List[int], queries: List[List[int]], k: int) -> bool:
        n: int = len(nums)
        total: int = 0
        cache: List[int] = [0] * (n + 1)

        for i in range(k):
            start, end, val = queries[i]

            cache[start] += val
            cache[end + 1] -= val

        for i in range(n):
            total += cache[i]
            if total < nums[i]:
                return False
        return True


def main() -> None:
    nums: List[int] = [2, 0, 2]
    queries: List[List[int]] = [[0, 2, 1], [0, 2, 1], [1, 1, 3]]
    res: int = Solution().minZeroArray(nums, queries)
    print(res)


if __name__ == "__main__":
    main()
