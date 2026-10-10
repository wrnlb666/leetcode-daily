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
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or k <= 1:
            return head

        lst: list[ListNode] = []
        curr: ListNode | None = head
        last: ListNode = ListNode(next=head)
        res: ListNode = last

        while True:
            if not curr:
                last.next = None
                break
            lst = []
            for i in range(k):
                lst.append(curr)
                curr = curr.next
                if not curr:
                    break
            if len(lst) < k:
                last.next = lst[0]
                break
            last.next = lst[-1]
            last = lst[0]
            for i in range(1, k):
                lst[i].next = lst[i - 1]

        return res.next


head = [1, 2, 3, 4, 5]
head = ListNode.from_list(head)
k = 2
print(Solution().reverseKGroup(head, k))
