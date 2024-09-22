

class Solution(object):
    def findKthNumber(self, n: int, k: int) -> int:
        curr: int = 1
        k -= 1

        def count_steps(n: int, prefix1: int, prefix2: int):
            steps: int = 0
            while prefix1 <= n:
                steps += min(n + 1, prefix2) - prefix1
                prefix1 *= 10
                prefix2 *= 10
            return steps

        while k > 0:
            step: int = count_steps(n, curr, curr + 1)
            if step <= k:
                curr += 1
                k -= step
            else:
                curr *= 10
                k -= 1

        return curr


def main() -> None:
    n: int = 957747794
    k: int = 424238336
    res: int = Solution().findKthNumber(n, k)
    print(res)


if __name__ == "__main__":
    main()
