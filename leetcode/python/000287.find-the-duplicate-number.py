# Reading: https://keithschwarz.com/interesting/code/?dir=find-duplicate


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # Start a fast and slow pointers until they meet
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # As soon as they meet, reset one pointer,
        # and move both pointers at the same speed until they meet again
        finder = 0
        while True:
            slow = nums[slow]
            finder = nums[finder]
            if slow == finder:
                break

        return finder
