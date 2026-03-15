import heapq
import math


class Solution:
    # Time complexity: O(n + k(log(n)))
    # Space complexity: O(1)
    def pickGifts(self, gifts: list[int], k: int) -> int:
        heapq.heapify_max(gifts)
        for _ in range(k):
            richest = heapq.heappop_max(gifts)
            heapq.heappush_max(gifts, math.floor(math.sqrt(richest)))
        return sum(gifts)

    # Time complexity: O(n + k(log(n)))
    # Space complexity: O(1)
    def pickGifts1(self, gifts: list[int], k: int) -> int:
        heapq.heapify_max(gifts)
        for _ in range(k):
            richest = heapq.heappop_max(gifts)
            heapq.heappush_max(gifts, math.isqrt(richest))
        return sum(gifts)
