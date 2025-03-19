from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def flip(s: int) -> None:
            for i in range(s, s + 3):
                nums[i] = 1 if nums[i] == 0 else 0

        res: int = 0
        for i in range(len(nums) - 2):
            n: int = nums[i]
            if n == 0:
                res += 1
                flip(i)
        return res if nums[-1] == 1 and nums[-2] == 1 else -1


def main() -> None:
    nums: List[int] = [0, 1, 1, 1]
    res: int = Solution().minOperations(nums)
    print(res)


if __name__ == "__main__":
    main()
