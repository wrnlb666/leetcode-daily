from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res: List[List[int]] = list()
        candidates = [v for v in candidates if v <= target]
        candidates.sort()
        def backtrack(target: int, totalIdx: int, path: List[int]):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return  # end
            for i in range(totalIdx, len(candidates)):
                if i > totalIdx and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(target - candidates[i], i + 1, path + [candidates[i]])
        backtrack(target, 0, list())
        return res



def main() -> None:
    candidates: List[int] = [10,1,2,7,6,1,5]
    target: int = 8
    res: List[List[int]] = Solution().combinationSum2(candidates, target)
    print(res)


if __name__ == "__main__":
    main()
