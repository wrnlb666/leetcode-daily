from typing import List, Tuple


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        table: List[Tuple[int, int]] = [(i, 0) for i in values]
        for i, v in enumerate(values):
            if i == 0:
                continue
            for j in range(i):
                num, val = table[j]
                val = max(val, num + values[i] + j - i)
                table[j] = (num, val)
        return max(list(zip(*table))[1])


def main() -> None:
    values: List[int] = [8,1,5,2,6]
    res: int = Solution().maxScoreSightseeingPair(values)
    print(res)


if __name__ == "__main__":
    main()
