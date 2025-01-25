from typing import List, Deque, Dict
from collections import deque


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int):
        nums_sorted: List[int] = sorted(nums)

        curr_group: int = 0
        num_to_group: Dict[int, int] = dict()
        num_to_group[nums_sorted[0]] = curr_group

        group_to_list: Dict[int, Deque[int]] = dict()
        group_to_list[curr_group] = deque([nums_sorted[0]])

        for i in range(1, len(nums)):
            if abs(nums_sorted[i] - nums_sorted[i - 1]) > limit:
                curr_group += 1

            num_to_group[nums_sorted[i]] = curr_group

            if curr_group not in group_to_list:
                group_to_list[curr_group] = deque()
            group_to_list[curr_group].append(nums_sorted[i])

        for i in range(len(nums)):
            num = nums[i]
            group = num_to_group[num]
            nums[i] = group_to_list[group].popleft()

        return nums


def main() -> None:
    nums: List[int] = [1, 5, 3, 9, 8]
    limit: int = 2
    res: List[int] = Solution().lexicographicallySmallestArray(nums, limit)
    print(res)


if __name__ == "__main__":
    main()
