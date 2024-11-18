from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)

        def index(code: List[int], i: int) -> int:
            return code[i % len(code)]

        res: List[int] = list()
        start, end = (k, 0) if k < 0 else (1, k+1)
        sum: int = 0
        for i in range(start, end):
            sum += index(code, i)
        res.append(sum)
        for i in range(1, len(code)):
            sum -= index(code, start)
            sum += index(code, end)
            start += 1
            end += 1
            res.append(sum)

        return res


def main() -> None:
    code: List[int] = [2,4,9,3]
    k: int = -2

    res: List[int] = Solution().decrypt(code, k)
    print(res)


if __name__ == "__main__":
    main()
