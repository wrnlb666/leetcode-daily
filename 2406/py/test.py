from typing import List, Tuple


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events: List[Tuple[int, int]] = list()

        for interval in intervals:
            events.append((interval[0], 1))
            events.append((interval[1] + 1, -1))

        events.sort(key=lambda x: (x[0], x[1]))
        print(events)

        curr: int = 0
        res: int = 0

        for e in events:
            curr += e[1]
            res = max(res, curr)

        return res


def main() -> None:
    intervals: List[List[int]] = [[5,10],[6,8],[1,5],[2,3],[1,10]]
    res: int = Solution().minGroups(intervals)
    print(res)


if __name__ == "__main__":
    main()
