from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n: int = len(nums)

        low: int = 0
        high: int = nums[n - 1] - nums[0]

        def bs(max_distance: int) -> int:
            count: int = 0
            left: int = 0

            for right in range(n):
                while nums[right] - nums[left] > max_distance:
                    left += 1
                count += right - left
            return count

        while low < high:
            mid: int = (low + high) // 2
            count: int = bs(mid)
            if count < k:
                low = mid + 1
            else:
                high = mid

        return low


def main() -> None:
    nums: List[int] = [1,6,1]
    k: int = 3
    res: int = Solution().smallestDistancePair(nums, k)
    print(res)


if __name__ == "__main__":
    main()
