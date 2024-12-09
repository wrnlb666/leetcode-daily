from typing import List, Tuple


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

        table: List[Tuple[int, int]] = list()
        left: int = 0
        for right in range(len(interval)):
            if not interval[right]:
                if left != right:
                    table.append((left, right))
                left = right + 1
        if left != len(interval):
            table.append((left, len(interval)))

        def check(s: int, e: int) -> bool:
            if not table:
                return False

            left: int = 0
            right: int = len(table) - 1
            index: int = len(table) - 1

            while left <= right:
                mid: int = (left + right) // 2
                if table[mid][0] == s:
                    index = mid
                    break
                elif table[mid][0] > s:
                    right = mid - 1
                else:
                    index = mid
                    left = mid + 1

            if s >= table[index][0] and e <= table[index][1]:
                return True
            return False

        res: List[bool] = list()
        for s, e in queries:
            if s == e:
                res.append(True)
                continue
            if check(s, e):
                res.append(True)
            else:
                res.append(False)

        return res


def main() -> None:
    nums: List[int] = [2,2,3,6,8,7,4,9]
    queries: List[List[int]] = [[2,3]]

    res: List[bool] = Solution().isArraySpecial(nums, queries)
    print(res)


if __name__ == "__main__":
    main()
