class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def rob(self, nums: list[int]) -> int:
        # Max if we skip first house VS skip last house
        # Edge case: input array of len(1)
        return max(self.helper(nums[:-1]), self.helper(nums[1:]), nums[0])

    def helper(self, nums: list[int]) -> int:
        one, two = 0, 0
        for n in nums:
            temp = max(n + one, two)
            one = two
            two = temp
        return max(one, two)
