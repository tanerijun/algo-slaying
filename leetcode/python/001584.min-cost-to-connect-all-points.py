import heapq


class Solution:
    # Prim's algorithm
    # Time complexity: O(n^2(log(n)))
    # Space complexity: O(n^2)
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        N = len(points)
        graph = {i: [] for i in range(N)}  # i: list of [cost, node]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append([dist, j])
                graph[j].append([dist, i])

        res = 0
        visited = set()
        min_heap = [[0, 0]]  # cost 0, node 0
        while len(visited) < N:
            cost, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            res += cost
            visited.add(i)

            for neighbor_cost, neighbor_node in graph[i]:
                if neighbor_node not in visited:
                    heapq.heappush(min_heap, [neighbor_cost, neighbor_node])

        return res
