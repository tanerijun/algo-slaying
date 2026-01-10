from collections import Counter


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def divideArray(self, nums: list[int]) -> bool:
        counter = Counter(nums)
        for v in counter.values():
            if v % 2 != 0:
                return False
        return True
