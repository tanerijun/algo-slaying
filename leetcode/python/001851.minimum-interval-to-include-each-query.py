import heapq


class Solution:
    # Brute force
    # Time complexity: O(n * m)
    # Space complexity: O(1)
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        res = []
        for query in queries:
            cur_min = float("inf")
            for interval in intervals:
                if interval[0] <= query <= interval[1]:
                    cur_min = min(cur_min, interval[1] - interval[0] + 1)
            res.append(-1 if cur_min == float("inf") else cur_min)
        return res

    # Time complexity: O(nlog(n) * mlog(m))
    # Space complexity: O(n + m)
    def minInterval2(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        intervals.sort()
        res = {}
        min_heap = []
        i = 0

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(min_heap, (r - l + 1, r))
                i += 1

            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            res[q] = min_heap[0][0] if min_heap else -1

        return [res[q] for q in queries]
