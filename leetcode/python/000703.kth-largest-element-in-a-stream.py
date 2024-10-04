import heapq
from typing import List


class KthLargest:

    # Time complexity: O(n*log(n)) because we have to pop until length is k.
    # If k is really small (e.g 1), we might have to pop close to n times.
    def __init__(self, k: int, nums: List[int]):
        # min heap with K largest integers
        self.min_heap, self.k = nums, k
        heapq.heapify(self.min_heap)  # O(n)

        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    # Time complexity: O(log(n))
    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
