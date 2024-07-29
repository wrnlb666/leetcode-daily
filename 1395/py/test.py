from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n: int = len(rating)
        res: int = 0

        for mid in range(n):
            left_smaller: int = 0
            right_larger: int = 0

            for left in range(mid - 1, -1, -1):
                if rating[left] < rating[mid]:
                    left_smaller += 1

            for right in range(mid + 1, n):
                if rating[right] > rating[mid]:
                    right_larger += 1

            res += left_smaller * right_larger

            left_larger = mid - left_smaller
            right_smaller = n - mid - 1 - right_larger

            res += left_larger * right_smaller

        return res


def main() -> None:
    rating: List[int] = [2,5,3,4,1]

    res: int = Solution().numTeams(rating)
    print(res)


if __name__ == "__main__":
    main()
