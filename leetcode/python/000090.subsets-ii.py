class Solution:
    # Time complexity: O(2^n)
    # Space complexity: O(n)
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        def backtrack(container, index):
            if index == len(nums):
                res.append(container.copy())
                return

            container.append(nums[index])
            backtrack(container, index + 1)

            container.pop()
            while index < len(nums) and index + 1 == nums[index]:
                index += 1
            backtrack(container, index + 1)

        backtrack([], 0)

        return res
