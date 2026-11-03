class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        res: int = 0
        for i in range(len(heights)):
            lowest: int = heights[i]
            curr: int = heights[i]
            res = max(res, curr)
            for j in range(i+1, len(heights)):
                block = heights[j]
                lowest = min(lowest, block)
                curr = lowest * (j-i+1)
                res = max(res, curr)

        return res


heights = [2,1,5,6,2,3]
print(Solution().largestRectangleArea(heights))
