from typing import List


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq: List[int] = [0] * 3
        left: int = 0
        right: int = 0
        res: int = 0

        while right < len(s):
            c: int = ord(s[right]) - ord('a')
            freq[c] += 1
            while all(f > 0 for f in freq):
                c: int = ord(s[left]) - ord('a')
                res += len(s) - right
                freq[c] -= 1
                left += 1
            right += 1

        return res


def main() -> None:
    s: str = "abcabc"
    res: int = Solution().numberOfSubstrings(s)
    print(res)


if __name__ == "__main__":
    main()
