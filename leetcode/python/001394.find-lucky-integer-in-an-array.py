from collections import Counter


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def findLucky(self, arr: list[int]) -> int:
        count = Counter(arr)
        res = -1
        for k, v in count.items():
            if k == v:
                res = max(res, k)
        return res
