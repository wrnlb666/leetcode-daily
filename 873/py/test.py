from typing import List, Dict


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n: int = len(arr)
        map: Dict[int, int] = {v: i for i, v in enumerate(arr)}
        cache: List[List[int]] = [[0] * n for _ in range(n)]
        res: int = 2
        for i in range(n):
            for j in range(i+1, n):
                last: int = arr[j] - arr[i]
                last_idx: int = map.get(last, -1)
                # print(arr[i], arr[j], last)
                if last_idx == -1 or last >= arr[i]:
                    cache[i][j] = 2
                else:
                    cache[i][j] = cache[last_idx][i] + 1
                    res = max(res, cache[i][j])
        return res if res > 2 else 0


def main() -> None:
    arr: List[int] = [1,2,3,4,5,6,7,8]
    res: int = Solution().lenLongestFibSubseq(arr)
    print(res)


if __name__ == "__main__":
    main()
