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


from heapq import heappush, heappop


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None
        pool: list[tuple[int, int]] = []
        for i in range(len(lists)):
            head: ListNode | None = lists[i]
            if not head:
                continue
            heappush(pool, (head.val, i))
            lists[i] = head.next
        res: ListNode = ListNode()
        curr: ListNode = res
        while pool:
            val, index = heappop(pool)
            curr.next = ListNode(val)
            new_head: ListNode | None = lists[index]
            if new_head:
                heappush(pool, (new_head.val, index))
                lists[index] = new_head.next
            curr = curr.next

        return res.next


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
lists = list(map(ListNode.from_list, lists))
print(Solution().mergeKLists(lists))
