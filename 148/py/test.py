# Definition for singly-linked list.
from typing import Self


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        curr: Self | None = self
        res: list[int] = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return str(res)

    @classmethod
    def from_list(cls, nums: list[int]) -> Self | None:
        head: Self = cls()
        curr: Self = head
        for n in nums:
            curr.next = cls()
            curr = curr.next
            curr.val = n
        return head.next


class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None

        lst: list[int] = []
        curr: ListNode | None = head
        while curr:
            lst.append(curr.val)
            curr = curr.next

        lst.sort()

        res: ListNode = ListNode()
        curr = res
        for n in lst:
            curr.next = ListNode(n)
            curr = curr.next

        return res.next


head = [-1, 5, 3, 4, 0]
head = ListNode.from_list(head)
print(Solution().sortList(head))
