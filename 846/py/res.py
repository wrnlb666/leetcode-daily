from collections import Counter

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        count: Counter = Counter(hand)
        print(count)
        
        for card in hand:
            if count[card] == 0:
                continue
            for i in range(groupSize):
                print(card, card+i, count[card+i])
                if count[card + i] > 0:
                    count[card + i] -= 1
                else:
                    return False
        return True


s:Solution = Solution()
hand: list[int] = [1,2,3,2,3,4,3,4,6,7,8,9]
groupSize: int = 3
print(s.isNStraightHand(hand, groupSize))

