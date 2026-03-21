class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        res = [0] * len(nums)
        i, j = 0, len(res) - 1
        for n in nums:
            if n % 2 == 0:
                res[i] = n
                i += 1
            else:
                res[j] = n
                j -= 1
        return res

    # Time complexity: O(n)
    # Space complexity: O(1)
    def sortArrayByParity2(self, nums: list[int]) -> list[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] % 2 != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1
        return nums

    # Time complexity: O(n(log(n)))
    # Space complexity: O(1)
    def sortArrayByParity3(self, nums: list[int]) -> list[int]:
        return sorted(nums, key=lambda x: x % 2 != 0)
