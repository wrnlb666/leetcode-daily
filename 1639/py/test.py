from typing import List, Final


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD: Final[int] = 1000000007
        word_length: int = len(words[0])
        target_length: int = len(target)
        char_frequency: List[List[int]] = [[0] * 26 for _ in range(word_length)]

        for word in words:
            for j in range(word_length):
                char_frequency[j][ord(word[j]) - ord("a")] += 1

        prev_count: List[int] = [0] * (target_length + 1)
        curr_count: List[int] = [0] * (target_length + 1)

        prev_count[0] = 1

        for curr_word in range(1, word_length + 1):
            curr_count = prev_count.copy()
            for curr_target in range(1, target_length + 1):
                cur_pos = ord(target[curr_target - 1]) - ord("a")

                curr_count[curr_target] += (
                    char_frequency[curr_word - 1][cur_pos]
                    * prev_count[curr_target - 1]
                ) % MOD
                curr_count[curr_target] %= MOD

            prev_count = curr_count.copy()

        return curr_count[target_length]


def main() -> None:
    words: List[str] = ["acca","bbbb","caca"]
    target: str = "aba"
    res: int = Solution().numWays(words, target)
    print(res)


if __name__ == "__main__":
    main()
