class Solution:
    def convert(self, num: int) -> int:
        s = str(num)
        n = len(s)
        l, r = (n - 1) // 2, n // 2
        s_list = list(s)
        while l >= 0:
            s_list[r] = s_list[l]
            r += 1
            l -= 1
        return int("".join(s_list))

    def previous_palindrome(self, num: int) -> float:
        left: int = 0
        right: int = num
        res: float = -float(1e18)
        while left <= right:
            mid: int = (right - left) // 2 + left
            palin: int = self.convert(mid)
            if palin < num:
                res = palin
                left = mid + 1
            else:
                right = mid - 1
        return res

    def next_palindrome(self, num: int) -> float:
        left: int = num
        right: int = int(1e18)
        res: float = float("-inf")
        while left <= right:
            mid: int = (right - left) // 2 + left
            palin: int = self.convert(mid)
            if palin > num:
                res = palin
                right = mid - 1
            else:
                left = mid + 1
        return res

    def nearestPalindromic(self, n: str) -> str:
        num: int = int(n)
        a: float = self.previous_palindrome(num)
        b: float = self.next_palindrome(num)
        return str(a) if abs(a - num) <= abs(b - num) else str(b)


def main() -> None:
    n: str = "0"
    res: str = Solution().nearestPalindromic(n)
    print(res)


if __name__ == "__main__":
    main()
