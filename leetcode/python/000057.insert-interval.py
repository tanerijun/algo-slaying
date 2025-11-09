class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        res = []

        for i in range(len(intervals)):
            # Not overlapping and come before current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # Not overlapping and come after current interval,
            # There is still a possibility that it overlaps with other intervals
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # Overlapping
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]

        res.append(newInterval)
        return res
