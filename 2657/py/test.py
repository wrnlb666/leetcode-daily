from typing import List, Set


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res: List[int] = [0] * len(A)

        num_a: Set[int] = set()
        num_b: Set[int] = set()

        for curr in range(len(A)):
            num_a.add(A[curr])
            num_b.add(B[curr])

            count: int = 0

            for n in num_a:
                if n in num_b:
                    count += 1

            res[curr] = count

        return res


def main() -> None:
    A: List[int] = [1, 3, 2, 4]
    B: List[int] = [3, 1, 2, 4]
    res: List[int] = Solution().findThePrefixCommonArray(A, B)
    print(res)


if __name__ == "__main__":
    main()
