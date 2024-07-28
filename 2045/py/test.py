from typing import List, Tuple, Deque
from collections import deque


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # adjacency list
        adj_list: List[List[int]] = [[] for _ in range(n + 1)]
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        # bfs
        queue: Deque[Tuple[int, int]] = deque([(1, 1)])
        dist1: List[int] = [-1 for _ in range(n + 1)]
        dist2: List[int] = [-1 for _ in range(n + 1)]
        dist1[1] = 0

        while queue:
            node, freq = queue.popleft()

            time_taken: int = dist1[node] if freq == 1 else dist2[node]

            if (time_taken // change) % 2 != 0:
                time_taken = change * (time_taken // change + 1) + time
            else:
                time_taken = time_taken + time

            for neighbor in adj_list[node]:
                if dist1[neighbor] == -1:
                    dist1[neighbor] = time_taken
                    queue.append((neighbor, 1))
                elif dist2[neighbor] == -1 and dist1[neighbor] != time_taken:
                    if neighbor == n:
                        return time_taken
                    dist2[neighbor] = time_taken
                    queue.append((neighbor, 2))

        return 0


def main() -> None:
    n: int = 6
    edges: List[List[int]] = [[1,2],[1,3],[2,4],[3,5],[5,4],[4,6]]
    time: int = 3
    change: int = 100

    res: int = Solution().secondMinimum(n, edges, time, change)
    print(res)


if __name__ == "__main__":
    main()
