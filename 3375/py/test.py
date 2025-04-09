from typing import List, Set


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums_set: Set[int] = set(nums)
        if any(map(lambda n: n < k, nums_set)):
            return -1
        return len(nums_set) - 1 if min(nums_set) == k else len(nums_set)


def main() -> None:
    nums: List[int] = [9,7,5,3]
    k: int = 1
    res: int = Solution().minOperations(nums, k)
    print(res)


if __name__ == "__main__":
    main()
