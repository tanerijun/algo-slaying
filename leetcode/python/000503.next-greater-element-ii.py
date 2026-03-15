class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        res = [-1] * len(nums)
        stack = []  # store indices of unresolved nums
        for i in range(len(nums) * 2):
            true_idx = i % len(nums)
            while stack and nums[true_idx] > nums[stack[-1]]:
                popped_idx = stack.pop()
                res[popped_idx] = nums[true_idx]
            if i < len(nums):
                stack.append(true_idx)
        return res
