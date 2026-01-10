class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def isArraySpecial(self, nums: list[int]) -> bool:
        is_prev_even = nums[0] % 2 == 0
        for i in range(1, len(nums)):
            if nums[i] % 2 == 0:
                if is_prev_even:
                    return False
                is_prev_even = True
            else:
                if not is_prev_even:
                    return False
                is_prev_even = False
        return True

    # Time complexity: O(n)
    # Space complexity: O(1)
    def isArraySpecial2(self, nums: list[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i - 1] % 2 == nums[i] % 2:
                return False
        return True

    # Time complexity: O(n)
    # Space complexity: O(1)
    def isArraySpecial3(self, nums: list[int]) -> bool:
        for i in range(1, len(nums)):
            if (nums[i - 1] + nums[i]) % 2 != 1:
                return False
        return True
