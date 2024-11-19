from typing import List, Set
from collections import Counter


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        curr_set: Set[int] = set()
        curr_sum: int = 0
        dup: Counter[int] = Counter()
        curr_dup: int = 0
        res: int = 0

        for i in range(k):
            if nums[i] in curr_set:
                dup[nums[i]] += 1
                curr_dup += 1
            else:
                curr_set.add(nums[i])
            curr_sum += nums[i]
        if not curr_dup:
            res = max(res, curr_sum)

        left: int = 0
        right: int = k
        while right < len(nums):
            if dup[nums[left]] > 0:
                dup[nums[left]] -= 1
                curr_dup -= 1
            else:
                curr_set.remove(nums[left])
            curr_sum -= nums[left]
            if nums[right] in curr_set:
                dup[nums[right]] += 1
                curr_dup += 1
            else:
                curr_set.add(nums[right])
            curr_sum += nums[right]
            if not curr_dup:
                res = max(res, curr_sum)

            left += 1
            right += 1

        return res


def main() -> None:
    nums: List[int] = [1,1,1,7,8,9]
    k: int = 3
    res: int = Solution().maximumSubarraySum(nums, k)
    print(res)


if __name__ == "__main__":
    main()
