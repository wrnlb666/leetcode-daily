from typing import List


class Solution:
    def constructDistancedSequence(self, target_number: int) -> List[int]:
        res: List[int] = [0] * (target_number * 2 - 1)

        used: List[bool] = [False] * (target_number + 1)

        self.rec(0, res, used, target_number)

        return res

    def rec(self, curr: int, res: List[int], used: List[bool], target: int) -> bool:
        if curr == len(res):
            return True

        if res[curr] != 0:
            return self.rec(curr + 1, res, used, target)

        for n2p in range(target, 0, -1):
            if used[n2p]:
                continue

            used[n2p] = True
            res[curr] = n2p

            if n2p == 1:
                if self.rec(curr + 1, res, used, target):
                    return True
            elif curr + n2p < len(res) and res[curr + n2p] == 0:
                res[curr + n2p] = n2p

                if self.rec(curr + 1, res, used, target):
                    return True

                res[curr + n2p] = 0

            res[curr] = 0
            used[n2p] = False

        return False


def main() -> None:
    n: int = 3
    res: List[int] = Solution().constructDistancedSequence(n)
    print(res)


if __name__ == "__main__":
    main()
