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

    # Prim's algorithm (optimized)
    # Time complexity: O(n^2)
    # Space complexity: O(n)
    def minCostConnectPoints1(self, points: list[list[int]]) -> int:
        n = len(points)
        # dist[i] stores the minimum weight to connect node i to the current MST
        # Initialize with infinity
        dist = [float("inf")] * n

        # We start from node 0, so distance to itself is 0
        dist[0] = 0

        in_mst = [False] * n
        res = 0
        nodes_connected = 0

        while nodes_connected < n:
            # Find the node with the smallest distance that isn't in MST yet
            # (In a sparse graph, we'd use a Heap here. In a dense graph, a simple loop is better)
            curr_node = -1
            min_val = float("inf")

            for i in range(n):
                if not in_mst[i] and dist[i] < min_val:
                    min_val = dist[i]
                    curr_node = i

            # Add that node to the MST
            res += min_val
            in_mst[curr_node] = True
            nodes_connected += 1

            # Update distances to all other nodes (Relaxation)
            # We calculate the distance on the fly (no graph storage needed)
            x1, y1 = points[curr_node]
            for next_node in range(n):
                if not in_mst[next_node]:
                    x2, y2 = points[next_node]
                    weight = abs(x1 - x2) + abs(y1 - y2)

                    # If this connection is cheaper than the currently known
                    # cheapest way to reach next_node, update it.
                    if weight < dist[next_node]:
                        dist[next_node] = weight

        return int(res)
