from typing import List


class Solution:
    def _sieve(self, limit: int) -> List[bool]:
        sieve: List[bool] = [True] * (limit + 1)
        sieve[0] = sieve[1] = False

        for n in range(2, int(limit**0.5) + 1):
            if sieve[n]:
                for val in range(n * n, limit + 1, n):
                    sieve[val] = False
        return sieve

    def closestPrimes(self, left: int, right: int) -> List[int]:
        cache: List[bool] = self._sieve(right)

        primes: List[int] = [num for num in range(left, right + 1) if cache[num]]

        if len(primes) < 2:
            return [-1, -1]

        diff: float = float("inf")
        res: List[int] = [-1, -1]

        for i in range(1, len(primes)):
            curr = primes[i] - primes[i - 1]
            if curr < diff:
                diff = curr
                res = [primes[i - 1], primes[i]]

        return res


def main() -> None:
    left: int = 10
    right: int = 19
    res: List[int] = Solution().closestPrimes(left, right)
    print(res)


if __name__ == "__main__":
    main()
