class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack: list[int] = []
        index: int = len(temperatures) - 1
        highest: int = 0
        while index >= 0:
            curr: int = temperatures[index]
            highest = max(highest, curr)
            if curr >= highest or not stack:
                temperatures[index] = 0
            for i, v in enumerate(stack):
                if v > curr:
                    temperatures[index] = len(temperatures) - i - index - 1
            stack.append(curr)
            index -= 1

        return temperatures


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution().dailyTemperatures(temperatures))
