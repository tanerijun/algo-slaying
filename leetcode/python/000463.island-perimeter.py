class Solution:
    # Time complexity: O(m * n)
    # Space complexity: O(1)
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                        nr, nc = r + dr, c + dc
                        if (
                            nr < 0
                            or nc < 0
                            or nr == rows
                            or nc == cols
                            or grid[nr][nc] == 0
                        ):
                            perimeter += 1
        return perimeter
