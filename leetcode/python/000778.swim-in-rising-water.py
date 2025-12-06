import heapq


class Solution:
    # Time complexity: O(n^2(log(n)))
    # Space complexity: O(n^2)
    def swimInWater(self, grid: list[list[int]]) -> int:
        min_heap = [[grid[0][0], 0, 0]]  # (time/max_height, r, c)
        visited = set()
        visited.add((0, 0))

        while min_heap:
            t, r, c = heapq.heappop(min_heap)

            if r == len(grid) - 1 and c == len(grid) - 1:
                return t

            for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < len(grid)
                    and 0 <= nc < len(grid)
                    and (nr, nc) not in visited
                ):
                    visited.add((nr, nc))
                    heapq.heappush(min_heap, [max(t, grid[nr][nc]), nr, nc])

        return -1  # impossible
