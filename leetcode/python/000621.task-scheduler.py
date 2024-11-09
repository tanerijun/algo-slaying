import heapq
from collections import Counter, deque


class Solution:
    # Time complexity: O(n*log(k))
    # Each task gets counted once, and gets processed in heap once
    # Space complexity: O(k), where k is number of unique tasks
    # We never store more than k items in any of the data structures
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        queue = deque()  # (clock cycle when op can be executed again, op count)
        clock = 0

        while maxHeap or queue:
            clock += 1

            if maxHeap:
                c = heapq.heappop(maxHeap)  # O(log(26))
                c += 1  # reduce count
                if c < 0:
                    queue.append((clock + n, c))

            if queue and queue[0][0] == clock:
                _, c = queue.popleft()
                heapq.heappush(maxHeap, c)  # O(log(26))

        return clock
