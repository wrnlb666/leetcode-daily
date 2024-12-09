from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        nums = [n % 2 for n in nums]
        interval: List[bool] = list()
        last: int = nums[0]
        for n in range(1, len(nums)):
            curr: int = nums[n]
            if curr == last:
                interval.append(False)
            else:
                interval.append(True)
            last = curr

        res: List[bool] = list()
        for q in queries:
            temp: bool = True
            if q[0] == q[1]:
                res.append(temp)
                continue
            for i in range(q[0], q[1]):
                temp &= interval[i]
                if not temp:
                    break
            res.append(temp)

        return res


def main() -> None:
    nums: List[int] = [3,4,1,2,6]
    queries: List[List[int]] = [[0,4]]

    res: List[bool] = Solution().isArraySpecial(nums, queries)
    print(res)


if __name__ == "__main__":
    main()
