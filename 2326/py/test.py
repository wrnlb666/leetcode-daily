from typing import List, Optional, Self, Tuple


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, l: List[int]) -> Optional[Self]:
        if not l:
            return None
        head: Self = cls(l[0])
        node: Self = head
        for n in l[1:]:
            node.next = cls(n)
            node = node.next
        return head


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res: List[List[int]] = [[-1 for _ in range(n)] for _ in range(m)]
        if not head:
            return res
        
        dirs: List[Tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir: int = 0
        def next_dir() -> None:
            nonlocal dir
            if dir >= 3:
                dir = 0
                return
            dir += 1

        curr: List[int] = [0, -1]
        m -= 1
        # n -= 1
        isH: bool = True

        def mov() -> None:
            nonlocal isH
            nonlocal head
            nonlocal res
            nonlocal curr
            nonlocal m
            nonlocal n
            x: int
            if isH:
                x = n
            else:
                x = m
            for _ in range(x):
                num: int = -1
                if head != None:
                    num = head.val
                    head = head.next
                curr[0] += dirs[dir][0]
                curr[1] += dirs[dir][1]
                print(curr[0], curr[1], num, flush=True)
                res[curr[0]][curr[1]] = num
            next_dir()
            if isH:
                n -= 1
            else:
                m -= 1
            isH = not isH
        
        while head != None:
            mov()
        
        return res

def main() -> None:
    m: int = 3
    n: int = 5
    head: List[int] = [3,0,2,6,8,1,7,9,4,2,5,5,0]

    res: List[List[int]] = Solution().spiralMatrix(m, n, ListNode.from_list(head))
    print(res)


if __name__ == "__main__":
    main()
