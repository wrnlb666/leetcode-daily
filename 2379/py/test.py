from typing import List


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res: int = 0
        n: int = len(blocks)
        left: int = 0
        right: int = k
        curr: int = 0
        for i in range(right):
            if blocks[i] == "B":
                curr += 1
        res = max(res, curr)
        while right < n:
            if blocks[left] == "B":
                curr -= 1
            if blocks[right] == "B":
                curr += 1
            res = max(res, curr)
            left += 1
            right += 1
        return k - res


def main() -> None:
    blocks: str = "WBBWWBBWBW"
    k: int = 7
    res: int = Solution().minimumRecolors(blocks, k)
    print(res)


if __name__ == "__main__":
    main()
