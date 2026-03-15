class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Find break point
        break_point_idx = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                break_point_idx = i - 1
                break

        if break_point_idx == -1:
            nums.reverse()
            return

        # Find swap target
        swap_target_idx = -1
        for i in range(len(nums) - 1, break_point_idx, -1):
            if nums[i] > nums[break_point_idx]:
                swap_target_idx = i
                break

        # Swap
        nums[break_point_idx], nums[swap_target_idx] = (
            nums[swap_target_idx],
            nums[break_point_idx],
        )

        # Reverse suffix
        nums[break_point_idx + 1 :] = nums[break_point_idx + 1 :][::-1]
