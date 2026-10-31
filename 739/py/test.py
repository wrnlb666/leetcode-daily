class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack: list[tuple[int, int]] = []
        i: int = 0
        while i < len(temperatures):
            curr: int = temperatures[i]
            while stack and curr > stack[-1][0]:
                _, index = stack.pop()
                temperatures[index] = i - index

            stack.append((curr, i))
            i += 1

        for _, i in stack:
            temperatures[i] = 0

        return temperatures


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution().dailyTemperatures(temperatures))
