import heapq
import math


class Solution:
    # Time complexity: O(n(log(n)))
    # Space complexity: O(n)
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # actually we don't need the sqrt (e.g sqrt(5) vs sqrt(4) -> we know which is larger even without the sqrt),
        # but I put it here for completion
        return sorted(points, key=lambda p: math.sqrt(p[0] ** 2 + p[1] ** 2))[:k]

    # Time complexity: O(n(log(k)))
    # Space complexity: O(k)
    def kClosestHeap(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for x, y in points:
            dist = -(x * x + y * y)
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        return [[x, y] for (dist, x, y) in heap]
