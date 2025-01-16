from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1: int = 0
        xor2: int = 0

        if len(nums2) % 2:
            for num in nums1:
                xor1 ^= num

        if len(nums1) % 2:
            for num in nums2:
                xor2 ^= num

        return xor1 ^ xor2


def main() -> None:
    nums1: List[int] = [2,1,3]
    nums2: List[int] = [10,2,5,0]
    res: int = Solution().xorAllNums(nums1, nums2)
    print(res)


if __name__ == "__main__":
    main()
