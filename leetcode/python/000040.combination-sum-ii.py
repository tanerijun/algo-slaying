class Solution:
    # Time complexity: O(2 ^ n)
    # Space complexity: O(n)
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res, temp = [], []

        def findCombinations(i, current_sum):
            if current_sum == target:
                res.append(temp.copy())
                return

            if i == len(candidates) or current_sum > target:
                return

            temp.append(candidates[i])
            findCombinations(i + 1, current_sum + candidates[i])
            temp.pop()

            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            findCombinations(i + 1, current_sum)

        findCombinations(0, 0)
        return res
