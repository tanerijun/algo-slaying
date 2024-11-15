class Solution:
    # Time complexity: O(n * m * 4^L) -> n: rows, m: cols, L: len(word)
    # Space complexity: O(L) -> Visited set and recursion depth can only be as long as L
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r: int, c: int, i: int):
            if i == len(word):
                return True

            if (
                r < 0
                or r >= ROWS
                or c < 0
                or c >= COLS
                or (r, c) in visited
                or board[r][c] != word[i]
            ):
                return False

            visited.add((r, c))

            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )

            visited.remove((r, c))

            return res

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True

        return False
