from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        return [n for n, _ in sorted(
            zip(nums, range(len(nums))),
            key=lambda t: self.mapped(mapping, t[0]) + t[1]/(10e4))]

    def mapped(self, mapping: List[int], num: int) -> int:
        if num == 0:
            return mapping[0]
        res: int = 0
        mul: int = 1
        while num > 0:
            res += mapping[num % 10] * mul
            num //= 10
            mul *= 10
        return res


def main() -> None:
    mapping: List[int] = [9,8,7,6,5,4,3,2,1,0]
    nums: List[int] = [0,1,2,3,4,5,6,7,8,9]
    res: List[int] = Solution().sortJumbled(mapping, nums)
    print(res)


if __name__ == '__main__':
    main()
