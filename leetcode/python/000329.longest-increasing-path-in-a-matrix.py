class Solution:
    # Time complexity: O(m * n)
    # Space complexity: O(m * n)
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        cache = {}
        rows, cols = len(matrix), len(matrix[0])

        def dfs(r, c):
            if (r, c) in cache:
                return cache[(r, c)]

            max_len = 1
            for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                new_r, new_c = r + dr, c + dc
                if (
                    0 <= new_r < rows
                    and 0 <= new_c < cols
                    and matrix[new_r][new_c] > matrix[r][c]
                ):
                    max_len = max(1 + dfs(new_r, new_c), max_len)

            cache[(r, c)] = max_len
            return max_len

        for r in range(rows):
            for c in range(cols):
                dfs(r, c)

        return max(cache.values())
