from collections import deque

class Solution:
    # Time complexity: O(m * n)
    # Space complexity: O(m * n)
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m, n = len(heights), len(heights[0])
        p_queue, a_queue = deque(), deque()
        p_seen, a_seen = set(), set()

        for i in range(n):
            p_queue.append((0, i))
            p_seen.add((0, i))

        for i in range(1, m):
            p_queue.append((i, 0))
            p_seen.add((i, 0))

        for i in range(m):
            a_queue.append((i, n - 1))
            a_seen.add((i, n - 1))

        for i in range(n - 1):
            a_queue.append((m - 1, i))
            a_seen.add((m - 1, i))

        def bfs(queue: deque[tuple[int, int]], seen: set[tuple[int, int]]):
            while queue:
                i, j = queue.popleft()
                for i_off, j_off in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                    r, c = i + i_off, j + j_off
                    if 0 <= r < m and 0 <= c < n and (r, c) not in seen and heights[r][c] >= heights[i][j]:
                        seen.add((r, c))
                        queue.append((r, c))

        bfs(p_queue, p_seen)
        bfs(a_queue, a_seen)
        return list(p_seen.intersection(a_seen))
