from typing import (
    List,
    Dict,
)

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cur_sum: int = 0
        res: int = 0
        sum: Dict[int, int] = {cur_sum: 1}

        for num in nums:
            cur_sum += num % 2
            res += sum.get(cur_sum - k, 0)
            sum[cur_sum] = sum.get(cur_sum, 0) + 1

        return res




def main() -> None:
    nums: List[int] = [1,1,2,1,1]
    k: int = 3

    res: int = Solution().numberOfSubarrays(nums, k)
    print(res)


if __name__ == '__main__':
    main()
