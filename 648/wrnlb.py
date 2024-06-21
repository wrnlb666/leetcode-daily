class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        shortestLength: int = 100
        dictionarySet: set[str] = set()
        for v in dictionary:
            if len(v) < shortestLength:
                shortestLength = len(v)
            dictionarySet.add(v)

        # print(dictionarySet)

        words: list[str] = sentence.split(" ")
        
        # print(words)

        for i, v in enumerate(words):
            length: int = len(v)
            if (length >= shortestLength):
                for j in range(shortestLength, length):
                    temp: str = v[:j]
                    if (temp in dictionarySet):
                        words[i] = temp
                        break

        return " ".join(words)




def main() -> None:
    dictionary: list[str] = ["cat","bat","rat"]
    sentence: str = "the cattle was rattled by the battery"
    print(Solution().replaceWords(dictionary, sentence))


if __name__ == "__main__":
    main()

