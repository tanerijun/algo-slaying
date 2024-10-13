import heapq


class Solution:
    # Time complexity: O(n(log(n)))
    # Space complexity: O(n)
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            if y != x:
                heapq.heappush(stones, y - x)
        return 0 if not stones else stones[0] * -1
