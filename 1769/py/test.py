from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res: List[int] = [0] * len(boxes)

        ball_left: int = 0
        move_left: int = 0
        for i in range(len(boxes)):
            res[i] += move_left
            ball_left += int(boxes[i])
            move_left += ball_left

        ball_right: int = 0
        move_right: int = 0
        for j in range(len(boxes)-1, -1, -1):
            res[j] += move_right
            ball_right += int(boxes[j])
            move_right += ball_right

        return res


def main() -> None:
    boxes: str = "110"
    res: List[int] = Solution().minOperations(boxes)
    print(res)


if __name__ == "__main__":
    main()
