from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def is_connected(src, target, visited, adj_list):
            visited[src] = True

            if src == target:
                return True

            is_found = False
            for adj in adj_list[src]:
                if not visited[adj]:
                    is_found = is_found or is_connected(adj, target, visited, adj_list)

            return is_found

        adj_list = [list() for _ in range(len(edges))]

        for edge in edges:
            visited = [False] * len(edges)

            if is_connected(edge[0] - 1, edge[1] - 1, visited, adj_list):
                return edge

            adj_list[edge[0] - 1].append(edge[1] - 1)
            adj_list[edge[1] - 1].append(edge[0] - 1)

        return list()


def main() -> None:
    edges: List[List[int]] = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    res: List[int] = Solution().findRedundantConnection(edges)
    print(res)


if __name__ == "__main__":
    main()
