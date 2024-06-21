class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        nums.sort()
        curr: int = -1
        move: int = 0
        print(nums)

        for n in nums:
            # print()
            # print(n, end=" ")
            if n <= curr:
                # print(n + (curr-n+1), end=" ")
                move += (curr-n+1)
                curr += 1
                # print(curr, end=" ")
            else:
                curr = n

        return move



def main() -> None:
    nums: list[int] = [3,2,1,2,1,7]
    res: int = Solution().minIncrementForUnique(nums)
    print("\n\n")
    print(res)

if __name__ == "__main__":
    main()
