class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        res = 1
        # strictly increasing
        l = 0
        for r in range(1, len(nums)):
            if nums[r] > nums[r - 1]:
                res = max(res, r - l + 1)
            else:
                l = r

        # strictly decreasing
        l = 0
        for r in range(1, len(nums)):
            print(nums[l], nums[r])
            if nums[r] < nums[r - 1]:
                res = max(res, r - l + 1)
            else:
                l = r

        return res
