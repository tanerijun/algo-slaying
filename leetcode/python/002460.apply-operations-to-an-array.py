class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def applyOperations(self, nums: list[int]) -> list[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        write = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[write] = nums[i]
                if i > write:
                    nums[i] = 0
                write += 1

        return nums
