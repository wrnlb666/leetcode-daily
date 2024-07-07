class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        

        if len(hand)%groupSize !=0 :
            return False
        else:
            hand.sort()
            dic ={}
            for i in hand:
                if i not in dic:
                    dic[i]=1
                else:
                    dic[i]+=1
            while hand:
                group = [hand.pop()]
                while len(group) < groupSize:
                    if not hand:
                        return False
                    if group[-1]-1 not in dic:
                        return False
                    else:
                        group.append(group[-1]-1)
                        dic[group[-1]]-=1
                        hand.remove(group[-1])
            return True


s = Solution()
hand: list[int] = [8,8,9,7,7,7,6,7,10,6]
groupSize: int = 2
print(s.isNStraightHand(hand, groupSize))

