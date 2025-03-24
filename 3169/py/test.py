from typing import List, Dict
from collections import defaultdict


class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        map: Dict[int, int] = defaultdict(int)
        prefix: int = 0
        res: int = 0
        prev: int = days

        for m in meetings:
            prev = min(prev, m[0])

            map[m[0]] += 1
            map[m[1] + 1] -= 1

        res += prev - 1
        for curr in sorted(map.keys()):
            if prefix == 0:
                res += curr - prev
            prefix += map[curr]
            prev = curr

        res += days - prev + 1
        return res


def main() -> None:
    days: int = 10
    meetings: List[List[int]] = [[5, 7], [1, 3], [9, 10]]
    res: int = Solution().countDays(days, meetings)
    print(res)


if __name__ == "__main__":
    main()
