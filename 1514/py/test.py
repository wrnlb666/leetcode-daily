from typing import List, DefaultDict, Tuple
from collections import defaultdict
import heapq


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph: DefaultDict[int, List[Tuple[int, float]]] = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        
        max_prob: List[float] = [0.0] * n
        max_prob[start] = 1.0
        
        pq: List[Tuple[float, int]] = [(-1.0, start)]    
        while pq:
            cur_prob, cur_node = heapq.heappop(pq)
            if cur_node == end:
                return -cur_prob
            for nxt_node, path_prob in graph[cur_node]:
                if -cur_prob * path_prob > max_prob[nxt_node]:
                    max_prob[nxt_node] = -cur_prob * path_prob
                    heapq.heappush(pq, (-max_prob[nxt_node], nxt_node))
        return 0.0


def main() -> None:
    n: int = 3
    edges: List[List[int]] = [[0, 1], [1, 2], [0, 2]]
    succProb: List[float] = [0.5, 0.5, 0.2]
    start: int = 0
    end: int = 2

    res: float = Solution().maxProbability(n, edges, succProb, start, end)
    print(res)


if __name__ == "__main__":
    main()
