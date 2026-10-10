# Definition for singly-linked list.
from typing import Self


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)

    @classmethod
    def from_list(cls, nums: list[int]) -> Self | None:
        head: Self = cls()
        curr: Self = head
        for n in nums:
            curr.next = cls()
            curr = curr.next
            curr.val = n
        return head.next

