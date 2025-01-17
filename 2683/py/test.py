from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        cache: List[int] = [0]
        for i in range(len(derived)):
            cache.append(derived[i] ^ cache[i])
        zero: bool = cache[0] == cache[-1]

        cache = [1]
        for i in range(len(derived)):
            cache.append(derived[i] ^ cache[i])
        one: bool = cache[0] == cache[-1]

        return zero or one


def main() -> None:
    derived: List[int] = [1,1,0]
    res: bool = Solution().doesValidArrayExist(derived)
    print(res)


if __name__ == "__main__":
    main()
