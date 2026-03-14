import bisect
from typing import (
    List,
)


class Solution:
    """
    @param nums: An integer array
    @param target: An integer
    @return: Is it a majority element
    """

    # Time complexity: O(n)
    # Space complexity: O(1)
    def is_majority_element(self, nums: List[int], target: int) -> bool:
        cur_n = 0
        cur_count = 0
        for n in nums:
            if cur_count == 0:
                cur_n = n
                cur_count = 1
            else:
                if n == cur_n:
                    cur_count += 1
                else:
                    cur_count -= 1

        if cur_n != target:
            return False

        n_target = nums.count(target)
        return n_target > len(nums) // 2

    def is_majority_element2(self, nums: List[int], target: int) -> bool:
        def find_first():
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] >= target:
                    r = m - 1
                else:
                    l = m + 1
            return r + 1

        i = find_first()
        return i + len(nums) // 2 < len(nums) and nums[i + len(nums) // 2] == target

    # Time complexity: O(log(n))
    # Space complexity: O(1)
    def is_majority_element3(self, nums: List[int], target: int) -> bool:
        i = bisect.bisect_left(nums, target)
        return i + len(nums) // 2 < len(nums) and nums[i + len(nums) // 2] == target
