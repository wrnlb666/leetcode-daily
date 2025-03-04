class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 1:
            if n % 3 == 2:
                return False
            n = n // 3
        return True


def main() -> None:
    n: int = 12
    res: bool = Solution().checkPowersOfThree(n)
    print(res)


if __name__ == "__main__":
    main()
