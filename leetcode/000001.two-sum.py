from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for x in range(len(nums)):
            current_num = nums[x]
            complement = target - current_num

            if complement in map:
                return [map[complement], x]
            else:
                map[current_num] = x

        return []
