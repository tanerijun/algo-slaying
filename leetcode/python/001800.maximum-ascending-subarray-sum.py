class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def maxAscendingSum(self, nums: list[int]) -> int:
        res = nums[0]
        current_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                current_sum = nums[i]
            res = max(res, current_sum)
        return res
