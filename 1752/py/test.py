from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        cache: List[int] = sorted(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[(i + j) % len(nums)] != cache[j]:
                    break
            else:
                return True
        return False


def main() -> None:
    nums: List[int] = [3,4,5,1,2]
    res: bool = Solution().check(nums)
    print(res)


if __name__ == "__main__":
    main()
