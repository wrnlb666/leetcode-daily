from typing import (
    List,
    Tuple,
    Dict,
    Optional,
)

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n: int = len(position)


        start: int = 1
        end: int = position[-1] // (m-1) + 1
        res: int = 0

        def check(position: List[int], m: int, x: int):
            count: int = 1
            last: int = position[0]
            for i in range(1, n):
                if position[i] - last >= x:
                    count += 1
                    if count == m:
                        return True
                    last = position[i]
            return False


        while start <= end:
            mid: int = (start + end) // 2
            if check(position, m, mid):
                start = mid + 1
                res = mid
            else:
                end = mid - 1

        return res


def main() -> None:
    position: List[int] = [20,73,90,55,21,52,26,46,57,51,95,13,30,68,32,15,31,44,23,82,17,33,12]
    m: int = 12

    res: int = Solution().maxDistance(position, m)
    print(res)


if __name__ == "__main__":
    main()
