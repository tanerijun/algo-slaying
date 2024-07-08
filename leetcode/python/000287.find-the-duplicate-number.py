# Floyd's cycle detection algorithm
# Reading: https://keithschwarz.com/interesting/code/?dir=find-duplicate
# Mathematical proof (animation): https://www.youtube.com/watch?v=PvrxZaH_eZ4


class Solution:
    # Other solutions include:
    # - brute force: for each number just loop through the array again and check for duplicate (O(n^2))
    # - sorting: sort and check from start (O(n log n))
    # - hash set: store and check from set for every element (time: O(n), space: O(n))

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
