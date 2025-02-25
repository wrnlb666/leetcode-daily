from typing import List, Final


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD: Final[int] = int(1e9 + 7)
        n: int = len(arr)

        for i in range(n):
            arr[i] %= 2

        even: List[int] = [0] * n
        odd: List[int] = [0] * n

        if arr[n - 1] == 0:
            even[n - 1] = 1
        else:
            odd[n - 1] = 1

        for num in range(n - 2, -1, -1):
            if arr[num] == 1:
                odd[num] = (1 + even[num + 1]) % MOD
                even[num] = odd[num + 1]
            else:
                even[num] = (1 + even[num + 1]) % MOD
                odd[num] = odd[num + 1]

        res: int = 0
        for odd_count in odd:
            res += odd_count
            res %= MOD

        return res


def main() -> None:
    arr: List[int] = [1, 3, 5]
    res: int = Solution().numOfSubarrays(arr)
    print(res)


if __name__ == "__main__":
    main()
