from typing import List


class Solution:
    def get_lis(self, v: List[int]) -> List[int]:
        lis_len = [1] * len(v)
        lis = [v[0]]

        for i in range(1, len(v)):
            index = self.get_lb(lis, v[i])

            if index == len(lis):
                lis.append(v[i])
            else:
                lis[index] = v[i]

            lis_len[i] = len(lis)

        return lis_len

    def get_lb(self, lis: List[int], target: int) -> int:
        left, right = 0, len(lis)
        while left < right:
            mid = left + (right - left) // 2
            if lis[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N = len(nums)

        lis_length = self.get_lis(nums)

        nums.reverse()
        lds_length = self.get_lis(nums)
        lds_length.reverse()

        res = len(nums)
        for i in range(N):
            if lis_length[i] > 1 and lds_length[i] > 1:
                res = min(res, N - lis_length[i] - lds_length[i] + 1)

        return res


def main() -> None:
    nums: List[int] = [23,47,63,72,81,99,88,55,21,33,32]
    res: int = Solution().minimumMountainRemovals(nums)
    print(res)


if __name__ == "__main__":
    main()
