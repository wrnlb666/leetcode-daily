from typing import List


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n1 = len(str1)
        n2 = len(str2)

        prev: List[str] = [str2[0:col] for col in range(n2 + 1)]

        for row in range(1, n1 + 1):
            curr: List[str] = [str1[0:row]] + ["" for _ in range(n2)]

            for col in range(1, n2 + 1):
                if str1[row - 1] == str2[col - 1]:
                    curr[col] = prev[col - 1] + str1[row - 1]
                else:
                    res1: str = prev[col]

                    res2: str = curr[col - 1]

                    curr[col] = (
                        res1 + str1[row - 1]
                        if len(res1) < len(res2)
                        else res2 + str2[col - 1]
                    )

            prev = curr

        return prev[n2]


def main() -> None:
    str1: str = "aaaaaaaa"
    str2: str = "aaaaaaaa"
    res: str = Solution().shortestCommonSupersequence(str1, str2)
    print(res)


if __name__ == "__main__":
    main()
