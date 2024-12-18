from typing import List, Tuple
from collections import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counter: Counter[int] = Counter()
        for c in s:
            counter[ord(c)] += 1
        chars: List[Tuple[int, int]] = list()
        for i, v in counter.items():
            chars.append((i, v))
        chars.sort(reverse=True)
        res: List[int] = list()
        index: int = 0
        last: int = 0
        repeat: int = 0
        while index < len(chars):
            # print(res)
            # print(chars)
            if chars[index][0] == last:
                if repeat == repeatLimit:
                    repeat = 1
                    for j in range(index+1, len(chars)):
                        if chars[j][1] != 0:
                            res.append(chars[j][0])
                            chars[j] = chars[j][0], chars[j][1]-1
                            last = chars[j][0]
                            break
                    else:
                        break
                else:
                    res.append(chars[index][0])
                    chars[index] = chars[index][0], chars[index][1]-1
                    repeat += 1
                    if chars[index][1] == 0:
                        for j in range(index+1, len(chars)):
                            if chars[j][1] != 0:
                                index = j
                                break
                        else:
                            break
            else:
                res.append(chars[index][0])
                last = chars[index][0]
                chars[index] = chars[index][0], chars[index][1]-1
                repeat = 1
                if chars[index][1] == 0:
                    for j in range(index+1, len(chars)):
                        if chars[j][1] != 0:
                            index = j
                            break
                    else:
                        break
        return "".join(map(chr, res))


def main() -> None:
    s: str = "cczazcc"
    repeatLimit: int = 3
    res: str = Solution().repeatLimitedString(s, repeatLimit)
    print(res)


if __name__ == "__main__":
    main()
