class Solution:
    # Time complexity: O(log(n))
    # Space complexity: O(1)
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (r - l) // 2

            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m

        return -1
