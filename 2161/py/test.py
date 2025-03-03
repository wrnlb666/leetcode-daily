from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less: List[int] = list()
        equal: List[int] = list()
        greater: List[int] = list()

        for n in nums:
            if n < pivot:
                less.append(n)
            elif n > pivot:
                greater.append(n)
            else:
                equal.append(n)

        return less + equal + greater


def main() -> None:
    nums: List[int] = [9,12,5,10,14,3,10]
    pivot: int = 10
    res: List[int] = Solution().pivotArray(nums, pivot)
    print(res)


if __name__ == "__main__":
    main()
