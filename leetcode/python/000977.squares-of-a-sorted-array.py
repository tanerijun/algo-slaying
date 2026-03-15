class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l, r = 0, len(nums) - 1
        res = [0] * len(nums)
        for i in range(len(res) - 1, -1, -1):
            if abs(nums[l]) >= abs(nums[r]):
                n = nums[l]
                l += 1
            else:
                n = nums[r]
                r -= 1
            res[i] = n * n
        return res
