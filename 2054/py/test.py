from typing import List, Tuple


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        table: List[Tuple[int, bool, int]] = list()
        for s, e, v in events:
            table.append((s, True, v))
            table.append((e+1, False, v))
        table.sort()
        
        res: int = 0
        last: int = 0
        for _, is_start, value in table:
            if is_start:
                res = max(res, last + value)
            else:
                last = max(last, value)

        return res


def main() -> None:
    events: List[List[int]] = [[1,3,2],[4,5,2],[2,4,3]]
    res: int = Solution().maxTwoEvents(events)
    print(res)


if __name__ == "__main__":
    main()
