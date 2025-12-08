from collections import deque


class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(n^2)
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0] == 1 or grid[len(grid) - 1][len(grid) - 1] == 1:
            return -1

        q = deque([(0, 0, 1)])
        visited = set()

        while q:
            r, c, length = q.popleft()

            if (r, c) in visited:
                continue
            visited.add((r, c))

            if r == len(grid) - 1 and c == len(grid) - 1:
                return length

            for dr, dc in [
                [-1, 0],
                [1, 0],
                [0, 1],
                [0, -1],
                [1, 1],
                [-1, -1],
                [1, -1],
                [-1, 1],
            ]:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < len(grid)
                    and 0 <= nc < len(grid)
                    and (nr, nc) not in visited
                    and grid[nr][nc] == 0
                ):
                    q.append((nr, nc, length + 1))

        return -1
