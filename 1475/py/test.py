from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res: List[int] = prices[:]
        stack: List[int] = list()

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                res[stack.pop()] -= prices[i]
            stack.append(i)

        return res


def main() -> None:
    prices: List[int] = [8,4,6,2,3]
    res: List[int] = Solution().finalPrices(prices)
    print(res)


if __name__ == "__main__":
    main()
