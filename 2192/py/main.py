from typing import (
    List,
    Set,
    Dict,
)

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges_dict: Dict[int, Set[int]] = {}
        for edge in edges:
            if edge[1] not in edges_dict:
                edges_dict[edge[1]] = set()
            edges_dict[edge[1]].add(edge[0])

        # print(edges_dict)
        
        cache: List[Set[int]] = [set() for _ in range(n)]
        def rec(node: int) -> Set[int]:
            if cache[node]:
                return cache[node]
            elif node not in edges_dict:
                cache[node] = set()
                return cache[node]
            else:
                local = set()
                for p in edges_dict[node]:
                    local.add(p)
                    local |= rec(p)
                cache[node] = local
                return local

        for e in edges_dict:
            rec(e)

        # print(cache)


        return [sorted(list(c)) for c in cache]


def main() -> None:
    n: int = 5
    edgeList: List[List[int]] = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

    res: int = Solution().getAncestors(n, edgeList)
    print(res)


if __name__ == "__main__":
    main()
