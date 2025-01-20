from typing import List, Tuple


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m: int = len(mat)
        n: int = len(mat[0])
        rm: List[int] = [n] * m
        rn: List[int] = [m] * n
        map: List[Tuple[int, int]] = list()
        index: int = 0
        for row in mat:
            for v in row:
                map.append((v, index))
                index += 1
        map.sort()
        print(map)
        print(arr)

        def bs(v: int) -> int:
            left: int = 0
            right: int = len(map)
            while left < right:
                mid: int = (left + right) // 2
                if v == map[mid][0]:
                    return map[mid][1]
                if v < map[mid][0]:
                    right = mid
                elif v > map[mid][0]:
                    left = mid
            return -1

        def check(index: int) -> bool:
            r: int = index // n
            c: int = index % n
            print(index, r, c)
            rm[r] -= 1
            rn[c] -= 1
            if rm[r] == 0 or rn[c] == 0:
                return True
            return False

        for i, v in enumerate(arr):
            if check(bs(v)):
                return i
        return -1


def main() -> None:
    arr: List[int] = [1,3,4,2]
    mat: List[List[int]] = [[1,4],[2,3]]
    res: int = Solution().firstCompleteIndex(arr, mat)
    print(res)


if __name__ == "__main__":
    main()
