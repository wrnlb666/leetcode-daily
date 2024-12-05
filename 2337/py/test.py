class Solution:
    def canChange(self, start: str, target: str) -> bool:
        t: str = target.replace('_', '')
        if start.replace('_', '') != t:
            return False
        si: int = 0
        ti: int = 0
        for c in t:
            while start[si] != c:
                si += 1
            si += 1
            while target[ti] != c:
                ti += 1
            ti += 1
            if c == 'L':
                if si < ti:
                    return False
            else:
                if si > ti:
                    return False
        return True


def main() -> None:
    start: str = "_LL__R__R_"
    target: str = "L___L___RR"

    res: bool = Solution().canChange(start, target)
    print(res)


if __name__ == "__main__":
    main()
