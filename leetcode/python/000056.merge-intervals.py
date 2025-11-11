class Solution:
    # Time complexity: O(nlog(n))
    # Space complexity: O(1)
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda i: i[0])
        res = [intervals[0]]

        for interval in intervals:
            if interval[0] <= res[-1][1]:
                res[-1][1] = max(interval[1], res[-1][1])
            else:
                res.append(interval)

        return res
