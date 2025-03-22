from typing import List, Dict, Set, Deque
from collections import defaultdict, deque


class Solution:
    def findAllRecipes(
        self,
        recipes: list[str],
        ingredients: list[list[str]],
        supplies: list[str],
    ) -> list[str]:
        supply_set: Set[str] = set(supplies)
        r2i: Dict[str, int] = {k: v for v, k in enumerate(recipes)}
        graph: Dict[str, List[str]] = defaultdict(list)
        in_degree: List[int] = [0] * len(recipes)

        for i, ingres in enumerate(ingredients):
            for ingre in ingres:
                if ingre not in supply_set:
                    graph[ingre].append(recipes[i])
                    in_degree[i] += 1

        queue: Deque[int] = deque(i for i, count in enumerate(in_degree) if count == 0)
        res: List[str] = list()

        while queue:
            i = queue.popleft()
            recipe = recipes[i]
            res.append(recipe)

            for depend in graph[recipe]:
                in_degree[r2i[depend]] -= 1
                if in_degree[r2i[depend]] == 0:
                    queue.append(r2i[depend])

        return res


def main() -> None:
    recipes: List[str] = ["bread"]
    ingredients: List[List[str]] = [["yeast", "flour"]]
    supplies: List[str] = ["yeast", "flour", "corn"]
    res: List[str] = Solution().findAllRecipes(recipes, ingredients, supplies)
    print(res)


if __name__ == "__main__":
    main()
