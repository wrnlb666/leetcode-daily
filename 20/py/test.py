class Solution:
    def isValid(self, s: str) -> bool:
        opening: dict[str, int] = {
            "(": 1,
            "[": 2,
            "{": 3,
        }
        closing: dict[str, int] = {
            ")": 1,
            "]": 2,
            "}": 3,
        }
        stack: list[int] = []
        for ch in s:
            if ch in opening:
                stack.append(opening[ch])
            else:
                if not stack:
                    return False
                expected = stack.pop()
                if expected != closing[ch]:
                    return False
        return not stack
