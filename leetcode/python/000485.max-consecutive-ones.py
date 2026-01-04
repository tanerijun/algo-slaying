class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count, res = 0, 0
        for n in nums:
            count = (count + 1) if n == 1 else 0
            res = max(res, count)
        return res
