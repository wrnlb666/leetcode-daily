from typing import (
    List,
    Tuple,
)


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        def use_power(min: int) -> int:
            return customers[min]

        def no_power(min: int) -> int:
            return customers[min] if grumpy[min] == 0 else 0

        length: int = len(customers)
        win_power: int = 0
        win_nopow: int = 0

        # first window
        for i in range(0, minutes):
            win_power += use_power(i)
            win_nopow += no_power(i)


        good: Tuple[int, int] = (win_power - win_nopow, 0)
        for i in range(1, length - minutes + 1):
            win_power = win_power - use_power(i - 1) + use_power(i + minutes - 1)
            win_nopow = win_nopow - no_power(i - 1) + no_power(i + minutes - 1)

            good = max(good, (win_power - win_nopow, i))

        index: int = good[1]
        for i in range(index, index + minutes):
            grumpy[i] = 0

        res: int = 0
        for i in range(length):
            res += customers[i] if grumpy[i] == 0 else 0

        return res


def main() -> None:
    customers: List[int] = [1,1,1,2,1,1,7,5]
    grumpy: List[int] = [0,1,0,1,0,1,0,1]
    minutes: int = 3
    res: int = Solution().maxSatisfied(customers, grumpy, minutes)
    print(res)

if __name__ == "__main__":
    main()
