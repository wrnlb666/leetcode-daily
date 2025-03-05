class Solution:
    def coloredCells(self, n: int) -> int:
        res: int = 1
        n = n - 1
        while n != 0:
            res = res + n * 4
            n = n - 1
        return res


def main() -> None:
    n: int = 3
    res: int = Solution().coloredCells(n)
    print(res)


if __name__ == "__main__":
    main()
