class Solution:
    # Time complexity: O(n * 4^n) - branch + appending str to res (remember str in python is immutable)
    # Space complexity: O(n)
    def letterCombinations(self, digits: str) -> list[str]:
        digitToLetters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def dfs(i, cur):
            if len(cur) == len(digits):
                res.append(cur)
                return

            for c in digitToLetters[digits[i]]:
                dfs(i + 1, cur + c)

        if digits:
            dfs(0, "")

        return res
