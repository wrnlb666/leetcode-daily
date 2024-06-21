class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0: int = 0
        c1: int = 0
        c2: int = 0
        for v in nums:
            if v == 0:
                c0 += 1
            elif v == 1:
                c1 += 1
            else:
                c2 += 1

        for i in range(0, c0):
            nums[i] = 0
        for i in range(c0, c0 + c1):
            nums[i] = 1
        for i in range(c0 + c1, c0 + c1 + c2):
            nums[i] = 2
            


def main() -> None:
    nums: list[int] = [2,0,2,1,1,0]
    Solution().sortColors(nums)
    print(nums)


if __name__ == "__main__":
    main()
