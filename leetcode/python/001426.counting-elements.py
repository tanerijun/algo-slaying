from collections import Counter


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def countElements(self, arr: list[int]) -> int:
        counter = Counter(arr)
        res = 0
        for k, v in counter.items():
            if k + 1 in counter:
                res += v
        return res
