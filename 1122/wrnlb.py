class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        map: dict[int, int] = {}
        for i, v in enumerate(arr2):
            map[v] = i

        def key(v: int) -> int:
            if v in map:
                return map[v]
            # since in constraints `1 <= arr1.length, arr2.length <= 1000`
            return v + 1001

        return sorted(arr1, key=key)
        


def main() -> None:
    arr1: list[int] = [2,3,1,3,2,4,6,7,9,2,19]
    arr2: list[int] = [2,1,4,3,9,6]
    print(Solution().relativeSortArray(arr1, arr2))


if __name__ == "__main__":
    main()
