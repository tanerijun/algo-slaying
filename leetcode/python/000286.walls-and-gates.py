from collections import deque
from typing import (
    List,
)


class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    # Time complexity: O(m * n)
    # Space complexity: O(m * n)
    def walls_and_gates(self, rooms: List[List[int]]):
        INF = 2**31 - 1
        rows, cols = len(rooms), len(rooms[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                    rooms[nr][nc] = rooms[r][c] + 1
                    q.append((nr, nc))
