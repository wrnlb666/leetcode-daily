class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n: int = len(heights)
        if not n:
            return 0

        stack: list[int] = []
        left: list[int] = [0] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []
        right: list[int] = [0] * n
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        print(left, right)
        candidates: list[int] = [
            (right[i] - left[i] - 1) * heights[i] for i in range(n)
        ]
        return max(candidates)


heights = [3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(Solution().largestRectangleArea(heights))
