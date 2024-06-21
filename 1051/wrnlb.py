

class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        count: int = 0
        expected: list[int] = sorted(heights)
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                count += 1
        return count


def main() -> None:
    heights: list[int] = [1,1,4,2,1,3]
    print(Solution().heightChecker(heights))


if __name__ == "__main__":
    main()
