class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # Only add "(" if open_n < n
        # Only add ")" if close < n
        # Stop when open_n == close_n == n

        res = []

        def backtrack(open_n, close_n, path):
            if open_n == close_n == n:
                res.append(path)
                return

            if open_n < n:
                backtrack(open_n + 1, close_n, path + "(")

            if close_n < open_n:
                backtrack(open_n, close_n + 1, path + ")")

        backtrack(0, 0, "")

        return res
