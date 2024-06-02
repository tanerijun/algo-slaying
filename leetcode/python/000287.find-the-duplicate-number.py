# Reading: https://keithschwarz.com/interesting/code/?dir=find-duplicate


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        finder = 0
        while True:
            slow = nums[slow]
            finder = nums[finder]
            if slow == finder:
                break

        return finder
