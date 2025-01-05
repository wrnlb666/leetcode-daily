from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n: int = len(s)
        cache: List[int] = [0] * n

        for shift in shifts:
            if shift[2] == 1:
                cache[shift[0]] += 1
                if shift[1] + 1 < n:
                    cache[shift[1] + 1] -= 1
            else:
                cache[shift[0]] -= 1
                if shift[1] + 1 < n:
                    cache[shift[1] + 1] += 1

        res: List[str] = list(s)
        counts: int = 0

        for i in range(n):
            counts = (counts + cache[i]) % 26
            if counts < 0:
                counts += 26

            shifted = chr((ord(s[i]) - 97 + counts) % 26 + 97)
            res[i] = shifted

        return "".join(res)


def main() -> None:
    s: str = "abc"
    shifts: List[List[int]] = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
    res: str = Solution().shiftingLetters(s, shifts)
    print(res)


if __name__ == "__main__":
    main()
