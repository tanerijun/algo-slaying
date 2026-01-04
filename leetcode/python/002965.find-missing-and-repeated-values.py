class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(n^2)
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        n = len(grid)
        s = set()
        duplicate, missing = -1, -1
        for i in range(n):
            for j in range(n):
                if duplicate == -1 and grid[i][j] in s:
                    duplicate = grid[i][j]
                s.add(grid[i][j])
        for i in range(1, n * n + 1):
            if i not in s:
                missing = i
                break
        return [duplicate, missing]
