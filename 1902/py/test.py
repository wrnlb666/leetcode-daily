from typing import Dict, Tuple


class Solution:
    def shortestCommonSupersequence(
        self, str1: str, str2: str, cache: Dict[Tuple[str, str], str] = dict()
    ) -> str:
        target: Tuple[str, str] = (str1, str2)
        if target in cache:
            return cache[target]

        if not str1 and not str2:
            return ""

        if not str1:
            return str2
        if not str2:
            return str1

        if str1[0] == str2[0]:
            cache[target] = str1[0] + self.shortestCommonSupersequence(
                str1[1:], str2[1:]
            )
            return cache[target]

        res1 = str1[0] + self.shortestCommonSupersequence(str1[1:], str2)
        res2 = str2[0] + self.shortestCommonSupersequence(str1, str2[1:])

        cache[target] = res1 if len(res1) < len(res2) else res2
        return cache[target]


def main() -> None:
    str1: str = "aaaaaaaa"
    str2: str = "aaaaaaaa"
    res: str = Solution().shortestCommonSupersequence(str1, str2)
    print(res)


if __name__ == "__main__":
    main()
