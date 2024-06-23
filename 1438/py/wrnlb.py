from typing import (
    List,
    Tuple,
)


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # slide window index
        start: int = 0

        # slide window current min and max
        small: Tuple[int, int] = (nums[0], 0)
        large: Tuple[int, int] = (nums[0], 0)

        # res
        res: int = 0
        curr: int = 0

        # loop
        for i in range(len(nums)):
            # print(small, large)
            if nums[i] > small[0] and nums[i] < large[0]:
                curr += 1
                continue
            if nums[i] == small[0]:
                curr += 1
                small = (nums[i], i)
                continue
            if nums[i] == large[0]:
                curr += 1
                large = (nums[i], i)
                continue

            if nums[i] > large[0]:
                large = (nums[i], i)
                # print(large)
                if large[0] - small[0] <= limit:
                    curr += 1
                    continue
                else:
                    # print(nums[start:i])
                    res = max(curr, res)

                    index: int = small[1]
                    small = large
                    start = i
                    for j in range(i-1, index, -1):
                        if large[0] - nums[j] > limit:
                            break
                        if nums[j] < small[0]:
                            small = (nums[j], j)
                        start = j

                    curr = i - start + 1

            if nums[i] < small[0]:
                small = (nums[i], i)
                # print(small)
                if large[0] - small[0] <= limit:
                    curr += 1
                    continue
                else:
                    # print(nums[start:i])
                    res = max(curr, res)

                    index: int = large[1]
                    large = small
                    start = i
                    for j in range(i-1, index, -1):
                        if nums[j] - small[0] > limit:
                            break
                        if nums[j] > large[0]:
                            large = (nums[j], j)
                        start = j
                
                    curr = i - start + 1

        # print(small, large, start)
        return max(curr, res)


def main() -> None:
    nums: List[int] = [4,2,2,2,4,4,2,2]
    limit: int = 0

    res: int = Solution().longestSubarray(nums, limit)
    print(res)


if __name__ == "__main__":
    main()
