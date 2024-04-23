class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def containsDuplicate(self, nums: list[int]) -> bool:
        map: dict[int, bool] = {}

        for num in nums:
            if num in map:
                return True

            map[num] = True

        return False
