from typing import List, Dict, Tuple


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        cache: Dict[int, int] = dict()
        for p, b in items:
            if p in cache:
                cache[p] = max(cache[p], b)
            else:
                cache[p] = b
        map: List[Tuple[int, int]] = list()
        for p, b in cache.items():
            map.append((p, b))
        map.sort()
        last: int = map[0][1]
        for i, (p, b) in enumerate(map):
            if b < last:
                map[i] = p, last
            else:
                last = b

        def bs(t: int) -> int:
            if t < map[0][0]:
                return 0
            left: int = 0
            right: int = len(map) - 1
            res: int = -1
            while left <= right:
                mid: int = (left + right) // 2

                if map[mid][0] < t:
                    res = mid
                    left = mid + 1
                elif map[mid][0] > t:
                    right = mid - 1
                else:
                    return map[mid][1]
            return map[res][1]

        return [bs(t) for t in queries]


def main() -> None:
    items: List[List[int]] = [[1,2],[3,2],[2,4],[5,6],[3,5]]
    queries: List[int] = [1,2,3,4,5,6]

    res: List[int] = Solution().maximumBeauty(items, queries)
    print(res)


if __name__ == "__main__":
    main()
