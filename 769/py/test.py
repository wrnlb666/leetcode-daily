from typing import List


class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        size: int = len(arr)
        res: int = 0
        sum: int = 0
        ssum: int = 0

        for i in range(size):
            sum += arr[i]
            ssum += i
            if sum == ssum:
                res += 1

        return res


def main() -> None:
    arr: List[int] = [4,3,2,1,0]
    res: int = Solution().maxChunksToSorted(arr)
    print(res)


if __name__ == "__main__":
    main()
