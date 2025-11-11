import heapq


class MedianFinder:
    def __init__(self):
        # small (maxHeap)
        # large (minHeap)
        self.small, self.large = [], []

    # Time complexity: O(log(n))
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, num * -1)  # to simulate maxHeap with minHeap

        # every element in small should be smaller than every element in large
        if self.small and self.large and self.small[0] * -1 > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # small and large should be evenly sized
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, val * -1)

    # Time complexity: O(1)
    def findMedian(self) -> float:
        # odd length
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        return (self.small[0] * -1 + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Follow up:
#
# 1. If all integer numbers from the stream are between 0 and 100, how would you optimize it?
# We can maintain an integer array of length 100 to store the count of each number along with a total count. Then, we can iterate over the array to find the middle value to get our median.
# Time and space complexity would be O(100) = O(1).
#
# 2. If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
# In this case, we need an integer array of length 100 and a hashmap for these numbers that are not in [0,100].
