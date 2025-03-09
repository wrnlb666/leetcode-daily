from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n: int = len(colors)
        res: int = 0
        count: int = 1
        last: int = colors[0]

        for i in range(1, n):
            if colors[i] == last:
                count = 1
                last = colors[i]
                continue
            count += 1
            if count >= k:
                res += 1
            last = colors[i]

        for i in range(k - 1):
            if colors[i] == last:
                break
            count += 1
            if count >= k:
                res += 1
            last = colors[i]

        return res


def main() -> None:
    colors: List[int] = [0, 1, 0, 1, 0]
    k: int = 3
    res: int = Solution().numberOfAlternatingGroups(colors, k)
    print(res)


if __name__ == "__main__":
    main()
