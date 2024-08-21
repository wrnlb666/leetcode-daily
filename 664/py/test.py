from typing import List
import itertools


class Solution:
    def strangePrinter(self, s: str) -> int:
        s = "".join(char for char, _ in itertools.groupby(s))

        cache = {}

        def min_turns(start, end) -> int:
            if start > end:
                return 0

            if (start, end) in cache:
                return cache[(start, end)]

            turns = 1 + min_turns(start + 1, end)

            for k in range(start + 1, end + 1):
                if s[k] == s[start]:
                    turns_with_match = min_turns(
                        start, k - 1
                    ) + min_turns(k + 1, end)
                    turns = min(turns, turns_with_match)

            cache[(start, end)] = turns
            return turns

        return min_turns(0, len(s) - 1)


def main() -> None:
    s: str = "aaabbb"
    res: int = Solution().strangePrinter(s)
    print(res)


if __name__ == "__main__":
    main()
