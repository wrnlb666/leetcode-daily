from typing import List, Deque
from collections import deque


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        matrix: List[List[bool]] = [
            [False for _ in range(numCourses)] for _ in range(numCourses)
        ]
        for a, b in prerequisites:
            matrix[a][b] = True

        cache: List[List[bool]] = [
            [False for _ in range(numCourses)] for _ in range(numCourses)
        ]

        def bfs() -> None:
            for i in range(numCourses):
                q: Deque[int] = deque([i])
                while q:
                    node = q.popleft()
                    for j, n in enumerate(matrix[node]):
                        if not n:
                            continue
                        if not cache[i][j]:
                            cache[i][j] = True
                            q.append(j)

        bfs()

        res: List[bool] = list()
        for q in queries:
            res.append(cache[q[0]][q[1]])
        return res


def main() -> None:
    numCourses: int = 3
    prerequisites: List[List[int]] = [[1, 2], [1, 0], [2, 0]]
    queries: List[List[int]] = [[1, 0], [1, 2]]
    res: List[bool] = Solution().checkIfPrerequisite(numCourses, prerequisites, queries)
    print(res)


if __name__ == "__main__":
    main()
