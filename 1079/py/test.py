from typing import Set
from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        seen: Set[str] = set()

        sorted_tiles: str = "".join(sorted(tiles))

        return self._gen(sorted_tiles, "", 0, seen) - 1

    def _factorial(self, n: int) -> int:
        if n <= 1:
            return 1

        res: int = 1
        for num in range(2, n + 1):
            res *= num
        return res

    def _permutation(self, seq: str) -> int:
        total = self._factorial(len(seq))

        for count in Counter(seq).values():
            total //= self._factorial(count)

        return total

    def _gen(self, tiles: str, curr: str, pos: int, seen: set) -> int:
        if pos >= len(tiles):
            if curr not in seen:
                seen.add(curr)
                return self._permutation(curr)
            return 0

        return self._gen(tiles, curr, pos + 1, seen) + self._gen(
            tiles, curr + tiles[pos], pos + 1, seen
        )


def main() -> None:
    tiles: str = "AAB"
    res: int = Solution().numTilePossibilities(tiles)
    print(res)


if __name__ == "__main__":
    main()
