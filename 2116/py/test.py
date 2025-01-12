from typing import List


class Solution:
    def canBeValid(self, s, locked):
        n: int = len(s)

        if n % 2 == 1:
            return False

        opens: List[int] = list()
        unlock: List[int] = list()

        for i in range(n):
            if locked[i] == "0":
                unlock.append(i)
            elif s[i] == "(":
                opens.append(i)
            elif s[i] == ")":
                if opens:
                    opens.pop()
                elif unlock:
                    unlock.pop()
                else:
                    return False

        while opens and unlock and opens[-1] < unlock[-1]:
            opens.pop()
            unlock.pop()

        if opens:
            return False

        return True


def main() -> None:
    s: str = "))()))"
    locked: str = "010100"
    res: bool = Solution().canBeValid(s, locked)
    print(res)


if __name__ == "__main__":
    main()
