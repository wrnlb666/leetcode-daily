from typing import List


class Solution:
    def find_min_distance(self, adj_list, n):
        dp = [0] * n
        dp[n - 1] = 0

        for current_node in range(n - 2, -1, -1):
            min_distance = n
            for neighbor in adj_list[current_node]:
                min_distance = min(min_distance, dp[neighbor] + 1)
            dp[current_node] = min_distance

        return dp[0]

    def shortestDistanceAfterQueries(self, n, queries):
        answer = []
        adj_list = [[] for _ in range(n)]

        for i in range(n - 1):
            adj_list[i].append(i + 1)

        for road in queries:
            u, v = road[0], road[1]
            adj_list[u].append(v)

            answer.append(self.find_min_distance(adj_list, n))

        return answer


def main() -> None:
    n: int = 5
    queries: List[List[int]] = [[2,4],[0,2],[0,4]]
    res: List[int] = Solution().shortestDistanceAfterQueries(n, queries)
    print(res)


if __name__ == "__main__":
    main()
