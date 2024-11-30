from typing import List, Dict, Counter
from collections import defaultdict


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        cr: Dict[int, List[int]] = defaultdict(list)
        cl: Counter[int] = Counter()
        for i in range(len(pairs)):
            s, e = pairs[i]
            cr[s].append(e)
            cl[e] += 1
        mid: List[int] = pairs[-1]
        for s, e in cr.items():
            if cl[s] < len(e):
                if len(e) == 1:
                    mid = [s, e[0]]
                    break
                for n in e:
                    if cl[n] <= len(cr[n]):
                        mid = [s, n]
                        break
        right = [mid]
        curr: int = mid[1]
        
        cr[mid[0]].remove(mid[1])
        if not cr[mid[0]]:
            del cr[mid[0]]

        while True:
            if curr not in cr:
                break
            new_curr: int = cr[curr].pop()
            right.append([curr, new_curr])
            if not cr[curr]:
                del cr[curr]
            curr = new_curr
        return right


def main() -> None:
    pairs: List[List[int]] = [[1,3],[3,2],[2,1]]
    res: List[List[int]] = Solution().validArrangement(pairs)
    print(res)


if __name__ == "__main__":
    main()
