

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        count = [0] * 3
        n = len(s)

        for c in s:
            count[ord(c) - ord("a")] += 1

        for i in range(3):
            if count[i] < k:
                return -1

        window = [0] * 3
        left, max_window = 0, 0

        for right in range(n):
            window[ord(s[right]) - ord("a")] += 1

            while left <= right and (
                count[0] - window[0] < k
                or count[1] - window[1] < k
                or count[2] - window[2] < k
            ):
                window[ord(s[left]) - ord("a")] -= 1
                left += 1

            max_window = max(max_window, right - left + 1)

        return n - max_window


def main() -> None:
    s: str = "aabaaaacaabc"
    k: int = 2

    res: int = Solution().takeCharacters(s, k)
    print(res)


if __name__ == "__main__":
    main()
