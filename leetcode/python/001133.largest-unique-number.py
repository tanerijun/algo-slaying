from collections import Counter


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def largestUniqueNumber(self, nums: list[int]) -> int:
        count = Counter(nums)
        res = -1
        for k, v in count.items():
            if v != 1:
                continue
            res = max(res, k)
        return res
