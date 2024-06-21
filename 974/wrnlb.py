class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        cs: int = 0
        map: dict[int, int] = {0: 1}
        count: int = 0
        
        for v in nums:
            cs += v
            if cs % k in map:
                count += map[cs % k]
                map[cs % k] += 1
                print(cs, map[cs % k])
            else:
                map[cs % k] = 1

        return count


def main() -> None:
    nums: list[int] = [4,5,0,-2,-3,1]
    k = 5
    print(Solution().subarraysDivByK(nums, k))


if __name__ == "__main__":
    main()
