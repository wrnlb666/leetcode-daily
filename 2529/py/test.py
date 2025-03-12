from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg: int = 0
        pos: int = 0
        zer: int = 0
        for n in nums:
            if n < 0:
                neg += 1
            elif n == 0:
                zer += 1
            else:
                break
        pos = len(nums) - zer - neg
        return max(neg, pos)


def main() -> None:
    nums: List[int] = [-2,-1,-1,1,2,3]
    res: int = Solution().maximumCount(nums)
    print(res)


if __name__ == "__main__":
    main()
