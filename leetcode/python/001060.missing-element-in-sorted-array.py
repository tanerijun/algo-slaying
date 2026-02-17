from typing import (
    List,
)


class Solution:
    """
    @param nums: An integer array
    @param k: An integer
    @return: Find the kth missing number in nums
    """

    # Check out LC 1539 which builds up to this
    # Time complexity: O(log(n))
    # Space complexity: O(1)
    def missing_element(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            missing_nums = nums[m] - nums[0] - m
            if missing_nums >= k:
                r = m - 1
            else:
                l = m + 1

        missing_nums = nums[r] - nums[0] - r
        return nums[r] + (k - missing_nums)
