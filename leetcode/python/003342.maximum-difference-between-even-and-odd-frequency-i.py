from collections import Counter


# Time complexity: O(n)
# Space complexity: O(1) - max char 26
class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        max_odd, min_even = float("-inf"), float("inf")
        for v in count.values():
            if v % 2 == 0:
                min_even = min(min_even, v)
            else:
                max_odd = max(max_odd, v)
        return int(max_odd - min_even)
