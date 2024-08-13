from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if((nums[i-1] ^ nums[i]) & 1) == 0:
                return False
        return True


def main() -> None:
    nums: List[int] = [2,1,4]
    res: int = Solution().isArraySpecial(nums)
    print(res)


if __name__ == "__main__":
    main()
