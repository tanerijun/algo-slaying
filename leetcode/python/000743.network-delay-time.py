import heapq
from collections import defaultdict


class Solution:
    # Time complexity: O(Elog(v))
    # Space complexity: O(V + E)
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        min_heap = [(0, k)]
        visited = set()
        max_time = 0

        while min_heap:
            time_to_current, current_node = heapq.heappop(min_heap)
            if current_node in visited:
                continue
            visited.add(current_node)
            max_time = time_to_current

            for neighbor, edge_weight in graph[current_node]:
                if neighbor not in visited:
                    time_to_neigbor = time_to_current + edge_weight
                    heapq.heappush(min_heap, (time_to_neigbor, neighbor))

        return max_time if len(visited) == n else -1
