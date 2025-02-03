from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc: int = 1
        dec: int = 1
        res: int = 1

        for pos in range(len(nums) - 1):
            if nums[pos + 1] > nums[pos]:
                inc += 1
                dec = 1
            elif nums[pos + 1] < nums[pos]:
                dec += 1
                inc = 1
            else:
                inc = dec = 1

            res = max(res, inc, dec)

        return res


def main() -> None:
    nums: List[int] = [1,4,3,3,2]
    res: int = Solution().longestMonotonicSubarray(nums)
    print(res)


if __name__ == "__main__":
    main()
