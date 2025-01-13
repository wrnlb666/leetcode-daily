from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        map: Counter[str] = Counter(s)
        res: int = 0
        for f in map.values():
            if f % 2 == 1:
                res += f - 1
            else:
                res += f - 2
        return len(s) - res


def main() -> None:
    s: str = "abaacbcbb"
    res: int = Solution().minimumLength(s)
    print(res)


if __name__ == "__main__":
    main()
