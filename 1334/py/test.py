from typing import List, Tuple
import heapq


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Adjacency list to store the graph
        adj_list: List[List[Tuple[int, int]]] = [[] for _ in range(n)]

        # Matrix to store shortest path distances from each city
        shortest_matrix: List[List[float]] = [[float("inf")] * n for _ in range(n)]

        # Initialize adjacency list and shortest path matrix
        for i in range(n):
            shortest_matrix[i][i] = 0  # Distance to itself is zero

        # Populate the adjacency list with edges
        for start, end, weight in edges:
            adj_list[start].append((end, weight))
            adj_list[end].append((start, weight))  # For undirected graph

        # Compute shortest paths from each city using Dijkstra's algorithm
        for i in range(n):
            self.dijkstra(n, adj_list, shortest_matrix[i], i)

        # Find the city with the fewest number of reachable cities within the distance threshold
        return self.get_city(n, shortest_matrix, distanceThreshold)

    # Dijkstra's algorithm to find shortest paths from a source city
    def dijkstra(self, n: int, adj_list: List[List[tuple]], shortest_distances: List[float], source: int):
        # Priority queue to process nodes with the smallest distance first
        queue: List[Tuple[int, int]] = [(0, source)]
        shortest_distances[:] = [float("inf")] * n
        shortest_distances[source] = 0  # Distance to itself is zero

        # Process nodes in priority order
        while queue:
            current_distance, current_city = heapq.heappop(queue)
            if current_distance > shortest_distances[current_city]:
                continue

            # Update distances to neighboring cities
            for neighbor_city, edge_weight in adj_list[current_city]:
                if (shortest_distances[neighbor_city] > current_distance + edge_weight):
                    shortest_distances[neighbor_city] = (current_distance + edge_weight)
                    heapq.heappush(queue, (shortest_distances[neighbor_city], neighbor_city))

    # Determine the city with the fewest number of reachable cities within the distance threshold
    def get_city(self, n: int, matrix: List[List[float]], threshold: int) -> int:
        res: int = -1
        count: int = n

        # Count number of cities reachable within the distance threshold for each city
        for i in range(n):
            reachable: int = sum(1 for j in range(n) if i != j and matrix[i][j] <= threshold)

            # Update the city with the fewest reachable cities
            if reachable <= count:
                count = reachable
                res = i
        return res


def main() -> None:
    n: int = 4
    edges: List[List[int]] = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
    distanceThreshold: int = 4

    res: int = Solution().findTheCity(n, edges, distanceThreshold)
    print(res)


if __name__ == "__main__":
    main()
