class Solution:
    # Time complexity: O(n!)
    # - First row, n choices for column; Second row, there are at most (n-1) valid columns, and so on.
    # Space complexity: O(n^2)
    # - Board is O(n^2), each set is O(n), recursion depth is O(n)
    def solveNQueens(self, n: int) -> list[list[str]]:
        col = set()
        pos_diag = set()  # (r + c)
        neg_diag = set()  # (r - c)
        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"
                backtrack(r + 1)

                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
