from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n: int = len(books)
        dp: List[int] = [0 for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = books[0][1]

        for i in range(2, n + 1):
            remaining: int = shelfWidth - books[i - 1][0]
            max_height: int = books[i - 1][1]
            dp[i] = books[i - 1][1] + dp[i - 1]

            j: int = i - 1
            while j > 0 and remaining - books[j - 1][0] >= 0:
                max_height = max(max_height, books[j - 1][1])
                remaining -= books[j - 1][0]
                dp[i] = min(dp[i], max_height + dp[j - 1])
                j -= 1

        return dp[n]


def main() -> None:
    books: List[List[int]] = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
    shelfWidth: int = 4

    res: int = Solution().minHeightShelves(books, shelfWidth)
    print(res)


if __name__ == "__main__":
    main()
