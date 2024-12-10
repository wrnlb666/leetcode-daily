from typing import List
import heapq


class Solution:
    def maximumLength(self, s: str) -> int:
        table: List[List[int]] = [list() for _ in range(26)]
        last: int = ord(s[0]) - 97
        count: int = 1
        for i in range(1, len(s)):
            c: int = ord(s[i]) - 97
            if c != last:
                if len(table[last]) < 3:
                    heapq.heappush(table[last], count)
                elif count > table[last][0]:
                    heapq.heappop(table[last])
                    heapq.heappush(table[last], count)
                last = c
                count = 1
            else:
                count += 1
        if len(table[last]) < 3:
            heapq.heappush(table[last], count)
        elif count > table[last][0]:
            heapq.heappop(table[last])
            heapq.heappush(table[last], count)

        res: int = -1
        for counts in table:
            if len(counts) == 0:
                continue
            if len(counts) == 1:
                c = counts[0]
                if c > 2:
                    res = max(res, c-2)
                continue
            if len(counts) == 2:
                c2, c1 = counts[0], counts[1]
                if c1 > c2+1:
                    if c1 > 2:
                        res = max(res, c1-2)
                    continue
                if c1 == c2:
                    if c1 > 2:
                        res = max(res, c1-1)
                    continue
                if c1 == c2+1:
                    res = max(res, c2)
                    continue
            if len(counts) == 3:
                c3 = heapq.heappop(counts)
                c2 = heapq.heappop(counts)
                c1 = heapq.heappop(counts)
                if c1 > c2+1:
                    if c1 > 2:
                        res = max(res, c1-2)
                    continue
                if c1 == c2 and c2 != c3:
                    if c1 > 2:
                        res = max(res, c1-1)
                    continue
                if c1 == c2+1:
                    res = max(res, c2)
                    continue
                if c1 == c2 and c2 == c3:
                    res = max(res, c1)
                    continue

        return res


def main() -> None:
    s: str = "ceeeeeeeeeeeebmmmfffeeeeeeeeeeeewww"
    res: int = Solution().maximumLength(s)
    print(res)


if __name__ == "__main__":
    main()
