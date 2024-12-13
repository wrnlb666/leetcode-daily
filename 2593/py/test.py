from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked: List[int] = list()
        res: int = 0
        for i in range(len(nums)):
            if not marked or nums[i] < marked[-1]:
                marked.append(nums[i])
            else:
                while marked:
                    res += marked.pop()
                    if marked:
                        marked.pop()
        while marked:
            res += marked.pop()
            if marked:
                marked.pop()

        return res


def main() -> None:
    nums: List[int] = [2,1,3,4,5,2]
    res: int = Solution().findScore(nums)
    print(res)


if __name__ == "__main__":
    main()
