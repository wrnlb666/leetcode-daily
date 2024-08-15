from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five: int = 0
        ten: int = 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            else:
                if ten > 0 and five > 0:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True


def main() -> None:
    bills: List[int] = [5,5,5,10,20]
    res: bool = Solution().lemonadeChange(bills)
    print(res)


if __name__ == "__main__":
    main()
