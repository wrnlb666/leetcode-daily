from typing import List


class ProductOfNumbers:
    prefix: List[int]
    size: int

    def __init__(self):
        self.prefix = [1]
        self.size = 0

    def add(self, num: int):
        if num == 0:
            self.prefix = [1]
            self.size = 0
        else:
            self.prefix.append(self.prefix[self.size] * num)
            self.size += 1

    def getProduct(self, k: int) -> int:
        if k > self.size:
            return 0
        return self.prefix[self.size] // self.prefix[self.size - k]
