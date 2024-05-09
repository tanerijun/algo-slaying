class Solution:
	# Time complexity: O(n)
	# Space complexity: O(n)
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix_products = [0] * len(nums)
        suffix_products = [0] * len(nums)
        for i in range(len(nums)):
            prefix_products[i] = nums[i] * prefix_products[i - 1] if i > 0 else nums[i]
        for i in range(len(nums) - 1, 0, -1):
            suffix_products[i] = nums[i] * suffix_products[i + 1] if i < len(nums) - 1 else nums[i]

        res = []
        for i in range(len(nums)):
            prefix = 1 if i == 0 else prefix_products[i - 1]
            postfix = 1 if i == len(nums) - 1 else suffix_products[i + 1]
            print(prefix, postfix)
            res.append(prefix * postfix)

        return res

# Solution1 optimized, since output array doesn't count as extra memory
class Solution2:
	# Time complexity: O(n)
	# Space complexity: O(1)
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix_products = [0] * len(nums)
        suffix_products = [0] * len(nums)
        for i in range(len(nums)):
            prefix_products[i] = nums[i] * prefix_products[i - 1] if i > 0 else nums[i]
        for i in range(len(nums) - 1, 0, -1):
            suffix_products[i] = nums[i] * suffix_products[i + 1] if i < len(nums) - 1 else nums[i]

        res = []
        for i in range(len(nums)):
            prefix = 1 if i == 0 else prefix_products[i - 1]
            postfix = 1 if i == len(nums) - 1 else suffix_products[i + 1]
            print(prefix, postfix)
            res.append(prefix * postfix)

        return res
