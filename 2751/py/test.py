from typing import (
    List,
    Deque,
)
from collections import (
    deque,
)


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n: int = len(positions)
        indices: List[int] = list(range(n))
        res: List[int] = []
        stack: Deque[int] = deque()

        indices.sort(key = lambda x: positions[x])

        for curr in indices:
            if directions[curr] == "R":
                stack.append(curr)
            else:
                while len(stack) != 0 and healths[curr] > 0:
                    top: int = stack.pop()

                    if healths[top] > healths[curr]:
                        healths[top] -= 1
                        healths[curr] = 0
                        stack.append(top)
                    elif healths[top] < healths[curr]:
                        healths[curr] -= 1
                        healths[top] = 0
                    else:
                        healths[curr] = 0
                        healths[top] = 0

        for index in range(n):
            if healths[index] > 0:
                res.append(healths[index])

        return res


def main() -> None:
    positions: List[int] = [5,4,3,2,1]
    healths: List[int] = [2,17,9,15,10]
    directions: str = "RRRRR"
    res: List[int] = Solution().survivedRobotsHealths(positions, healths, directions)

    print(res)


if __name__ == "__main__":
    main()
