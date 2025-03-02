from typing import List, Dict


class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        map: Dict[int, int] = dict()

        for nums in nums1:
            map[nums[0]] = nums[1]

        for nums in nums2:
            map[nums[0]] = map.get(nums[0], 0) + nums[1]

        res: List[List[int]] = list()
        for k, v in sorted(map.items()):
            res.append([k, v])

        return res


def main() -> None:
    nums1: List[List[int]] = [[1, 2], [2, 3], [4, 5]]
    nums2: List[List[int]] = [[1, 4], [3, 2], [4, 1]]
    res: List[List[int]] = Solution().mergeArrays(nums1, nums2)
    print(res)


if __name__ == "__main__":
    main()
