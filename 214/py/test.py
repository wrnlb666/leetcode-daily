class Solution:
    def shortestPalindrome(self, s: str) -> str:
        len_s = len(s)
        rev_str = s[::-1]

        for i in range(len_s):
            if s[: len_s - i] == rev_str[i:]:
                return rev_str[:i] + s
        return ""


def main() -> None:
    s: str = "aacecaaa"
    res: str = Solution().shortestPalindrome(s)
    print(res)


if __name__ == "__main__":
    main()
