class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if ((len(hand) % groupSize) != 0):
            return False

        hand.sort()
        # print(hand)

        data: list[list[int]] = []
        index: int = -1
        for v in hand:
            if (index == -1):
                index += 1
                data.append([v, 1])
            elif (data[index][0] == v):
                data[index][1] += 1
            else:
                index += 1
                data.append([v, 1])

        # print(data)

        res: list[list[int]] = []
        ri: int = -1
        shouldBreak: bool = False
        while (not shouldBreak):
            for i in range(groupSize):
                if (i == 0):
                    ri += 1
                    res.append([data[i][0]])
                    data[i][1] -= 1
                else:
                    if (len(data) <= i):
                        return False
                    res[ri].append(data[i][0])
                    data[i][1] -= 1
                    if (res[ri][i] != res[ri][0]+i):
                        return False

            i: int = 0
            for _ in range(groupSize):
                if (data[i][1] == 0):
                    data.pop(i)
                else:
                    i += 1


            if (len(data) == 0):
                shouldBreak = True

        # print(res)
        return True


s = Solution()
hand: list[int] = [8,8,9,7,7,7,6,7,10,6]
groupSize: int = 2
print(s.isNStraightHand(hand, groupSize))

