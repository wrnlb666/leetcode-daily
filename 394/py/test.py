class Solution:
    def decodeString(self, s: str) -> str:
        index: int = 0

        def isnum(idx: int) -> bool:
            return ord("0") <= ord(s[idx]) <= ord("9")

        def getnum() -> int:
            nonlocal index
            n = 0
            while isnum(index):
                n *= 10
                n += ord(s[index]) - ord("0")
                index += 1
            return n if n != 0 else 1

        def foo() -> str:
            nonlocal index
            times = getnum()
            res: str = ""
            index += 1
            while s[index] != "]":
                if s[index] == "[" or isnum(index):
                    res += foo()
                else:
                    res += s[index]
                index += 1
            return res * times

        res: str = ""
        while index < len(s):
            if isnum(index):
                res += foo()
            else:
                res += s[index]
            index += 1
        return res


s = "3[a]2[bc]"
print(Solution().decodeString(s))
