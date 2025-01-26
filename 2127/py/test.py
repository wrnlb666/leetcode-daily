from typing import List, Deque
from collections import deque


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n: int = len(favorite)
        in_degree: List[int] = [0] * n

        for person in range(n):
            in_degree[favorite[person]] += 1

        q: Deque[int] = deque()
        for person in range(n):
            if in_degree[person] == 0:
                q.append(person)
        depth: List[int] = [1] * n

        while q:
            current_node: int = q.popleft()
            next_node: int = favorite[current_node]
            depth[next_node] = max(depth[next_node], depth[current_node] + 1)
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                q.append(next_node)

        longest_cycle: int = 0
        two_cycle_invitations: int = 0

        for person in range(n):
            if in_degree[person] == 0:
                continue

            cycle_length: int = 0
            current: int = person
            while in_degree[current] != 0:
                in_degree[current] = 0
                cycle_length += 1
                current = favorite[current]

            if cycle_length == 2:
                two_cycle_invitations += depth[person] + depth[favorite[person]]
            else:
                longest_cycle = max(longest_cycle, cycle_length)

        return max(longest_cycle, two_cycle_invitations)


def main() -> None:
    favorite: List[int] = [2,2,1,2]
    res: int = Solution().maximumInvitations(favorite)
    print(res)


if __name__ == "__main__":
    main()
