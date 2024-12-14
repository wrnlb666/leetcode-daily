from typing import List, Dict
from collections import defaultdict


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        freq: Dict[int, int] = defaultdict(int)
        left: int = 0
        right: int = 0
        res: int = 0

        while right < len(nums):
            freq[nums[right]] = freq[nums[right]] + 1

            while max(freq) - min(freq) > 2:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            res += right - left + 1
            right += 1

        return res


def main() -> None:
    nums: List[int] = [5,4,2,4]
    res: int = Solution().continuousSubarrays(nums)
    print(res)
    

if __name__ == "__main__":
    main()
