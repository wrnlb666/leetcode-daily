from typing import List


class Solution:
    def applyOperations(self, res: List[int]) -> List[int]:
        n: int = len(res)

        for i in range(n - 1):
            if res[i] == res[i + 1] and res[i] != 0:
                res[i] *= 2
                res[i + 1] = 0

        index: int = 0
        for i in range(n):
            if res[i] != 0:
                res[index] = res[i]
                index += 1

        while index < n:
            res[index] = 0
            index += 1

        return res


def main() -> None:
    nums: List[int] = [1, 2, 2, 1, 1, 0]
    res: List[int] = Solution().applyOperations(nums)
    print(res)


if __name__ == "__main__":
    main()
