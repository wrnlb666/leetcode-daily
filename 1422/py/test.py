

class Solution:
    def maxScore(self, s: str) -> int:
        zero: int = 0
        ones: int = 0
        for c in s:
            if c == '0':
                zero += 1
            else:
                ones += 1

        res: int = 0
        curr_zero: int = 0
        curr_ones: int = 0
        for i in range(len(s)-1):
            c = s[i]
            if c == '0':
                curr_zero += 1
            else:
                curr_ones += 1
            res = max(res, curr_zero + ones - curr_ones)
        return res


def main() -> None:
    s: str = "011101"
    res: int = Solution().maxScore(s)
    print(res)


if __name__ == "__main__":
    main()
