from typing import List, Set


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        buf: Set[int] = set()
        zero_count: int = 0
        for n in arr:
            buf.add(n)
            if n == 0:
                zero_count += 1
        for n in arr:
            if 2 * n in buf:
                if n != 0:
                    return True
                if n == 0 and zero_count != 1:
                    return True
        return False


def main() -> None:
    arr: List[int] = [10,2,5,3]
    res: bool = Solution().checkIfExist(arr)
    print(res)


if __name__ == "__main__":
    main()
