class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i2: int = 0
        l1 = len(str1)
        l2 = len(str2)

        for i1 in range(l1):
            if i2 < l2 and (
                str1[i1] == str2[i2]
                or ord(str1[i1]) + 1 == ord(str2[i2])
                or ord(str1[i1]) - 25 == ord(str2[i2])
            ):
                i2 += 1

        return i2 == l2


def main() -> None:
    str1: str = "abc"
    str2: str = "ad"

    res: bool = Solution().canMakeSubsequence(str1, str2)
    print(res)


if __name__ == "__main__":
    main()
