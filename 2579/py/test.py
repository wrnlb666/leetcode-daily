class Solution:
    def coloredCells(self, n: int) -> int:
        return 2 * n * (n-1) + 1


def main() -> None:
    n: int = 3
    res: int = Solution().coloredCells(n)
    print(res)


if __name__ == "__main__":
    main()
