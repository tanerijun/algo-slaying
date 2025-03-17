class Solution:
    # Time complexity: O(m * n)
    # Space complexity: O(m * n)
    def maxAreaOfIsland(self, grid: List[List[int]] -> int):
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        visited = set()
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                area = dfs(r, c)
                max_area = max(max_area, area)
                       
        return max_area
