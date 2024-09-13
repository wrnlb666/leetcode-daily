from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix: List[int] = list()
        sum: int = 0
        prefix.append(sum)
        for n in arr:
            sum ^= n
            prefix.append(sum)
        res: List[int] = list()
        for s, e in queries:
            res.append(prefix[e + 1] ^ prefix[s])
        return res


def main() -> None:
    arr: List[int] = [1,3,4,8]
    queries: List[List[int]] = [[0,1],[1,2],[0,3],[3,3]]

    res: List[int] = Solution().xorQueries(arr, queries)
    print(res)


if __name__ == "__main__":
    main()
