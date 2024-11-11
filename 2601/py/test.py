from typing import List
import math


class Solution:
    def isprime(self, n: int):
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                return False
        return True

    def primeSubOperation(self, nums: List[int]):
        maxElement: int = max(nums)
        
        previous_prime: List[int] = [0] * (maxElement + 1)
        for i in range(2, maxElement + 1):
            if self.isprime(i):
                previous_prime[i] = i
            else:
                previous_prime[i] = previous_prime[i - 1]

        for i in range(len(nums)):
            if i == 0:
                bound: int = nums[0]
            else:
                bound = nums[i] - nums[i - 1]
            if bound <= 0:
                return False
            largest_prime = previous_prime[bound - 1]
            nums[i] -= largest_prime

        return True


def main() -> None:
    nums: List[int] = [4,9,6,10]
    res: bool = Solution().primeSubOperation(nums)
    print(res)


if __name__ == "__main__":
    main()
