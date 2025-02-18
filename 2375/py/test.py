from typing import List


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res: List[str] = list()

        def rec(curr_i: int, curr_c: int, p: str) -> int:
            if curr_i != len(p):
                if p[curr_i] == "I":
                    rec(curr_i + 1, curr_i + 1, p)
                else:
                    curr_c = rec(curr_i + 1, curr_c, p)
            res.append(str(curr_c + 1))
            return curr_c + 1

        rec(0, 0, pattern)
        return "".join(res[::-1])


def main() -> None:
    pattern: str = "IIIDIDDD"
    res: str = Solution().smallestNumber(pattern)
    print(res)


if __name__ == "__main__":
    main()
