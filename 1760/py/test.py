from typing import List
import math


class Solution:
    def minimumSize(self, nums: List[int], max_operations: int):
        left = 1
        right = max(nums)

        while left < right:
            mid = (left + right) // 2
            if self.valid(mid, nums, max_operations):
                right = mid
            else:
                left = mid + 1

        return left


    def valid(self, mid, nums, max_operations):
        total = 0

        for num in nums:
            oper = math.ceil(num / mid) - 1
            total += oper

            if total > max_operations:
                return False
        return True


def main() -> None:
    nums: List[int] = [9]
    maxOperations: int = 2

    res: int = Solution().minimumSize(nums, maxOperations)
    print(res)


if __name__ == "__main__":
    main()
