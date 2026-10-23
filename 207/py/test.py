from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        edges: dict[int, list[int]] = defaultdict(list)
        visited: list[int] = [0 for _ in range(numCourses)]
        for co, pre in prerequisites:
            edges[pre].append(co)

        def dfs(u: int) -> bool:
            nonlocal visited
            if u not in edges:
                visited[u] = 2
                return True
            else:
                visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    if not dfs(v):
                        return False
                elif visited[v] == 1:
                    return False
            visited[u] = 2
            return True

        for i in range(numCourses):
            if visited[i] == 0 and not dfs(i):
                return False
        return True


numCourses = 2
prerequisites = [[0, 1]]
print(Solution().canFinish(numCourses, prerequisites))
