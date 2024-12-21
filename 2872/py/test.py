from typing import List, Dict, Set, Deque
from collections import deque, defaultdict


class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        if n < 2:
            return 1

        component_count: int = 0
        graph: Dict[int, Set[int]] = defaultdict(set)

        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)

        queue: Deque[int] = deque(
            node for node, neighbors in graph.items() if len(neighbors) == 1
        )

        while queue:
            current_node: int = queue.popleft()
            neighbor_node = (
                next(iter(graph[current_node])) if graph[current_node] else -1
            )

            # Remove the edge between current and neighbor
            if neighbor_node >= 0:
                graph[neighbor_node].remove(current_node)

            # Check divisibility of the current node's value
            if values[current_node] % k == 0:
                component_count += 1
            else:
                values[neighbor_node] += values[current_node]

            # If the neighbor becomes a leaf node, add it to the queue
            if neighbor_node >= 0 and len(graph[neighbor_node]) == 1:
                queue.append(neighbor_node)

        return component_count


def main() -> None:
    n: int = 5
    edges: List[List[int]] = [[0,2],[1,2],[1,3],[2,4]]
    values: List[int] = [1,8,1,4,4]
    k: int = 6
    res: int = Solution().maxKDivisibleComponents(n, edges, values, k)
    print(res)


if __name__ == "__main__":
    main()
