class Solution:
    def punishmentNumber(self, n: int) -> int:
        def partition(string_num: str, target: int) -> bool:
            if not string_num and target == 0:
                return True
            if target < 0:
                return False
            for i in range(len(string_num)):
                left = string_num[: i + 1]
                right = string_num[i + 1 :]
                left_num = int(left)
                if partition(right, target - left_num):
                    return True
            return False

        res: int = 0
        for curr in range(1, n + 1):
            num: int = curr * curr
            if partition(str(num), curr):
                res += num
        return res


def main() -> None:
    n: int = 10
    res: int = Solution().punishmentNumber(n)
    print(res)


if __name__ == "__main__":
    main()
