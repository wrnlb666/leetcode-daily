class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            start = s.find(part)
            s = s[:start] + s[start + len(part) :]
        return s


def main() -> None:
    s: str = "daabcbaabcbc"
    part: str = "abc"
    res: str = Solution().removeOccurrences(s, part)
    print(res)


if __name__ == "__main__":
    main()
