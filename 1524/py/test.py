from typing import List, Final


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD: Final[int] = int(1e9 + 7)
        n: int = len(arr)
        res: int = 0

        for i in range(n):
            curr: int = 0
            for j in range(i, n):
                curr += arr[j]
                if curr % 2 != 0:
                    res += 1

        return res % MOD


def main() -> None:
    arr: List[int] = [1,3,5]
    res: int = Solution().numOfSubarrays(arr)
    print(res)


if __name__ == "__main__":
    main()
