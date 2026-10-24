from typing import Self


class Trie:
    children: list[Self | None]
    ended: bool

    def __init__(self):
        self.children = [None] * 26
        self.ended = False

    def insert(self, word: str) -> None:
        words = [ord(c) - 97 for c in word]
        node = self
        for ch in words:
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.ended = True

    def search(self, word: str) -> bool:
        words = [ord(c) - 97 for c in word]
        node = self
        for ch in words:
            if not node.children[ch]:
                return False
            node = node.children[ch]
        return node.ended

    def startsWith(self, prefix: str) -> bool:
        words = [ord(c) - 97 for c in prefix]
        node = self
        for ch in words:
            if not node.children[ch]:
                return False
            node = node.children[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
