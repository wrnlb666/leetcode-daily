from typing import List


class Solution:
    def minimumTotalDistance(self, robots: List[int], factories: List[List[int]]) -> int:
        robots.sort()
        factories.sort()

        factory_positions = []
        for factory in factories:
            for i in range(factory[1]):
                factory_positions.append(factory[0])

        robot_count = len(robots)
        factory_count = len(factory_positions)
        next_dist = [0 for _ in range(factory_count + 1)]
        current = [0 for _ in range(factory_count + 1)]

        for i in range(robot_count - 1, -1, -1):
            if i != robot_count - 1:
                next_dist[factory_count] = int(1e12)

            current[factory_count] = int(1e12)

            for j in range(factory_count - 1, -1, -1):
                assign = (
                    abs(robots[i] - factory_positions[j]) + next_dist[j + 1]
                )

                skip = current[j + 1]
                current[j] = min(assign, skip)

            next_dist = current[:]

        return current[0]

def main() -> None:
    robot: List[int] = [0,4,6]
    factory: List[List[int]] = [[2,2],[6,2]]
    res: int = Solution().minimumTotalDistance(robot, factory)
    print(res)


if __name__ == "__main__":
    main()
