from typing import List


class Solution:
    def dfs(
        self, node: int, adj: List[List[int]], visit: List[bool], inStack: List[bool]
    ):
        if inStack[node]:
            return True
        if visit[node]:
            return False
        visit[node] = True
        inStack[node] = True
        for neighbor in adj[node]:
            if self.dfs(neighbor, adj, visit, inStack):
                return True
        inStack[node] = False
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n: int = len(graph)

        visit: List[bool] = [False] * n
        inStack: List[bool] = [False] * n

        for i in range(n):
            self.dfs(i, graph, visit, inStack)

        res: List[int] = list()
        for i in range(n):
            if not inStack[i]:
                res.append(i)

        return res


def main() -> None:
    graph: List[List[int]] = [[1, 2], [2, 3], [5], [0], [5], [], []]
    res: List[int] = Solution().eventualSafeNodes(graph)
    print(res)


if __name__ == "__main__":
    main()
