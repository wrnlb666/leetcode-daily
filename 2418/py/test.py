from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [n for _, n in sorted(zip(heights, names), reverse=True)]


def main() -> None:
    names: List[str] = ["Mary", "John", "Emma"]
    heights: List[int] = [180, 165, 170]
    res: List[str] = Solution().sortPeople(names, heights)
    print(res)


if __name__ == "__main__":
    main()
