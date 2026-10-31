class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack: list[tuple[int, int]] = []
        index: int = 0
        while index < len(temperatures):
            curr: int = temperatures[index]
            new_stack: list[tuple[int, int]] = []
            for i, v in enumerate(stack):
                if curr > v[0]:
                    temperatures[v[1]] = index - v[1]
                else:
                    new_stack.append(v)
            stack = new_stack

            stack.append((curr, index))
            index += 1

        for _, index in stack:
            temperatures[index] = 0

        return temperatures


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution().dailyTemperatures(temperatures))
