# Definition for a Node.
from typing import Self


class Node:
    def __init__(self, x: int, next: Self | None = None, random: Self | None = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node | None) -> Node | None:
        if not head:
            return None
        dic: dict[Node, Node] = {}
        curr: Node | None = head
        while curr:
            dic[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            nc = dic[curr]
            if curr.next:
                nc.next = dic[curr.next]
            if curr.random:
                nc.random = dic[curr.random]
            curr = curr.next

        return dic[head]
