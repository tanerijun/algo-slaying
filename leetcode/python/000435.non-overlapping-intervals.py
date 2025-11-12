class Solution:
    # Time complexity: O(nlog(n))
    # Space complexity: O(1)
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda i: i[0])
        cur_last = intervals[0]
        to_remove = 0

        for interval in intervals[1:]:
            if interval[0] >= cur_last[1]:
                cur_last = interval
                continue
            to_remove += 1
            if interval[1] < cur_last[1]:
                cur_last = interval

        return to_remove

    # Time complexity: O(nlog(n))
    # Space complexity: O(1)
    def eraseOverlapIntervals2(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda i: i[1])
        cur_last = intervals[0]
        non_overlapping_count = 1

        for interval in intervals[1:]:
            if interval[0] >= cur_last[1]:
                non_overlapping_count += 1
                cur_last = interval

        return len(intervals) - non_overlapping_count
