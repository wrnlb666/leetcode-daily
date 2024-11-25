from typing import List, Set, Deque
from collections import deque


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        directions: List[List[int]] = [
            [1, 3],
            [0, 2, 4],
            [1, 5],
            [0, 4],
            [1, 3, 5],
            [2, 4],
        ]

        def _swap(state, i: int, j: int) -> str:
            state_list = list(state)
            state_list[i], state_list[j] = state_list[j], state_list[i]
            return "".join(state_list)

        target: str = "123450"
        start_state: str = "".join(str(num) for row in board for num in row)

        visited: Set[str] = set()
        queue: Deque[str] = deque([start_state])
        visited.add(start_state)

        moves: int = 0

        while queue:
            for _ in range(len(queue)):
                current_state: str = queue.popleft()

                if current_state == target:
                    return moves

                zero_pos: int = current_state.index("0")
                for new_pos in directions[zero_pos]:
                    next_state: str = _swap(current_state, zero_pos, new_pos)

                    if next_state in visited:
                        continue

                    visited.add(next_state)
                    queue.append(next_state)
            moves += 1

        return -1


def main() -> None:
    board: List[List[int]] = [[1,2,3],[4,0,5]]
    res: int = Solution().slidingPuzzle(board)
    print(res)


if __name__ == "__main__":
    main()
