from typing import Type, Self

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    @classmethod
    def from_list(cls, iter: list[int]) -> Self:
        node: ListNode|None = ListNode(iter[0])
        if len(iter) == 1:
            node.next = None
        else:
            node.next = cls.from_list(iter[1:])
        return node

    def print(self) -> None:
        node: ListNode|None = self
        while node:
            print(f"{node.val}|", end=" ")
            node = node.next
        print()


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode|None:
        n1: int = 0
        n2: int = 0
        e: int = 0

        temp: ListNode | None = l1
        while temp:
            n1 += temp.val * (10 ** e)
            temp = temp.next
            e += 1

        e = 0
        temp = l2
        while temp:
            n2 += temp.val * (10 ** e)
            temp = temp.next
            e += 1

        res: int = n1 + n2
        # print(n1, n2, res)

        def rec(remain: int, first: bool) -> ListNode|None:
            if remain == 0:
                if first:
                    return ListNode()
                else:
                    return None
            else:
                first = False
                digit: int = remain % 10
                ret: ListNode = ListNode(digit)
                ret.next = rec(remain // 10, False)
                return ret
        
        return rec(res, True)


def main() -> None:
    l1: ListNode|None
    l2: ListNode|None
    output: ListNode|None
    
    l1 = ListNode.from_list([2,4,3])
    l2 = ListNode.from_list([5,6,4])

    Solution().addTwoNumbers(l1, l2).print()

if __name__ == "__main__":
    main()
