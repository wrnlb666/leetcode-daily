from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqrt_c: int = int(sqrt(c)) + 1
        for a in range(sqrt_c):
            b: float = sqrt(c-a*a)
            if b % 1 == 0:
                print(a, " ", b)
                return True

        return False


def main() -> None:
    c: int = 6
    res: bool = Solution().judgeSquareSum(c)
    print(res)

if __name__ == "__main__":
    main()
