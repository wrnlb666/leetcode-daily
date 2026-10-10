from typing import Self


class Node:
    prev: Self | None
    next: Self | None
    val: int

    def __init__(
        self,
        key: int = -1,
        val: int = -1,
        prev: Self | None = None,
        next: Self | None = None,
    ) -> None:
        self.prev = prev
        self.next = next
        self.key = key
        self.val = val


class Queue:
    head: Node
    tail: Node
    len: int

    def __init__(self):
        head = Node()
        tail = Node()
        head.next = tail
        tail.prev = head
        self.head = head
        self.tail = tail
        self.len = 0

    def __repr__(self) -> str:
        res: list[tuple[int, int]] = []
        curr: Node = self.head.next
        while curr != self.tail:
            res.append((curr.key, curr.val))
            curr = curr.next
        return str(res)

    def __len__(self):
        return self.len

    def pop(self) -> Node:
        node = self.head.next
        if node != self.tail:
            self.len -= 1
            self.head.next = node.next
            node.next.prev = self.head
        return node

    def append(self, key: int = -1, val: int = -1) -> Node:
        self.len += 1
        node = Node(key, val, prev=self.tail.prev, next=self.tail)
        self.tail.prev.next = node
        self.tail.prev = node
        return node

    def move2end(self, node: Node) -> None:
        if node.next == self.tail:
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.tail.prev
        node.next = self.tail
        node.prev.next = node
        node.next.prev = node


class LRUCache:
    cache: dict[int, Node]
    lru: Queue
    cap: int

    def __init__(self, capacity: int):
        self.cache = {}
        self.lru = Queue()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.lru.move2end(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        cache = self.cache
        if key in cache:
            node = self.cache[key]
            self.lru.move2end(node)
            node.val = value
        elif len(self.lru) < self.cap:
            node = self.lru.append(key, value)
            self.cache[key] = node
        else:
            old_node = self.lru.pop()
            del cache[old_node.key]
            node = self.lru.append(key, value)
            self.cache[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
