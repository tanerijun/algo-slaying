class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix_products = [0] * len(nums)
        suffix_products = [0] * len(nums)
        for i in range(len(nums)):
            prefix_products[i] = nums[i] * nums[i - 1] if i > 0 else 1
        for i in range(len(nums) - 1, 0, -1):
            suffix_products[i] = nums[i] * nums[i + 1] if i < len(nums) - 1 else 1

        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = (
                prefix_products[i - 1]
                if i > 0
                else 1 * suffix_products[i + 1] if i < len(nums) - 1 else 1
            )
        return res
