class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def bits_count(n: int) -> int:
            res: int = 0
            while n:
                res += n & 1
                n = n >> 1
            return res

        bits: int = bits_count(num2)
        res: int = 0
        for i in range(32):
            if num1 & (1 << (31 - i)):
                res |= 1 << (31 - i)
                bits -= 1
                if not bits:
                    break
        else:
            i: int = 0
            while bits:
                if not res & (1 << i):
                    res |= 1 << i
                    bits -= 1
                i += 1
        return res


def main() -> None:
    num1: int = 1
    num2: int = 12
    res: int = Solution().minimizeXor(num1, num2)
    print(res)


if __name__ == "__main__":
    main()
