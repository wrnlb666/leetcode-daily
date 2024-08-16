from typing import List, Tuple


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        smallest: Tuple[int, int]
        largest: Tuple[int, int]
        smallest2: Tuple[int, int]
        largest2: Tuple[int, int]

        if arrays[0][0] < arrays[1][0]:
            smallest = (0, arrays[0][0])
            smallest2 = (1, arrays[1][0])
        else:
            smallest = (1, arrays[1][0])
            smallest2 = (0, arrays[0][0])

        if arrays[0][-1] > arrays[1][-1]:
            largest = (0, arrays[0][-1])
            largest2 = (1, arrays[1][-1])
        else:
            largest = (1, arrays[1][-1])
            largest2 = (0, arrays[0][-1])

        for l in range(2, len(arrays)):
            if arrays[l][0] < smallest2[1]:
                if arrays[l][0] < smallest[1]:
                    smallest2 = smallest
                    smallest = (l, arrays[l][0])
                else:
                    smallest2 = (l, arrays[l][0])

            if arrays[l][-1] > largest2[1]:
                if arrays[l][-1] > largest[1]:
                    largest2 = largest
                    largest = (l, arrays[l][-1])
                else:
                    largest2 = (l, arrays[l][-1])

        print(smallest, smallest2)
        print(largest, largest2)
        if smallest[0] != largest[0]:
            return largest[1] - smallest[1]
        return max(largest[1] - smallest2[1], largest2[1] - smallest[1])


def main() -> None:
    arrays: List[List[int]] = [[-1,1],[-3,1,4],[-2,-1,0,2]]
    res: int = Solution().maxDistance(arrays)
    print(res)


if __name__ == "__main__":
    main()
