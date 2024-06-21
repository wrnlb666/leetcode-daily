class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        return sum(abs(seat - student) for seat, student in zip(sorted(seats), sorted(students)))


def main() -> None:
    seats: list[int] = [3,1,5]
    students: list[int] = [2,7,4]
    print(Solution().minMovesToSeat(seats, students))


if __name__ == "__main__":
    main()
