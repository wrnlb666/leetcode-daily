from typing import Deque
from collections import deque


class Solution:
    def minLength(self, s: str) -> int:
        stack: Deque[str] = deque()
        s_len: int = len(s)
        i: int = 0
        while i < s_len:
            if s[i] == 'B':
                if stack and stack[-1] == 'A':
                    stack.pop()
                else:
                    stack.append('B')
            elif s[i] == 'D':
                if stack and stack[-1] == 'C':
                    stack.pop()
                else:
                    stack.append('D')
            else:
                stack.append(s[i])
            i += 1

        return len(stack)


def main() -> None:
    s: str = "ABFCACDB"
    res: int = Solution().minLength(s)
    print(res)


if __name__ == "__main__":
    main()
