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
        def sort(head: ListNode | None, tail: ListNode | None) -> ListNode | None:
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head
            slow = fast = head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            mid = slow
            return merge(sort(head, mid), sort(mid, tail))

        def merge(left: ListNode | None, right: ListNode | None) -> ListNode | None:
            res = ListNode(0)
            curr, cl, cr = res, left, right
            while cl and cr:
                if cl.val <= cr.val:
                    curr.next = cl
                    cl = cl.next
                else:
                    curr.next = cr
                    cr = cr.next
                curr = curr.next
            if cl:
                curr.next = cl
            elif cr:
                curr.next = cr
            return res.next

        return sort(head, None)


head = [-1, 5, 3, 4, 0]
head = ListNode.from_list(head)
print(Solution().sortList(head))
