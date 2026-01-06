class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def isMonotonic(self, nums: list[int]) -> bool:
        state = 0  # 0 undecided, -1 monotonic decreasing, +1 monotonic increasing
        for i in range(1, len(nums)):
            if state == 0:
                state = (
                    1 if nums[i] > nums[i - 1] else -1 if nums[i] < nums[i - 1] else 0
                )
                continue
            if (state == -1 and nums[i] > nums[i - 1]) or (
                state == 1 and nums[i] < nums[i - 1]
            ):
                return False
        return True

    # Time complexity: O(n)
    # Space complexity: O(1)
    def isMonotonic2(self, nums: list[int]) -> bool:
        increasing, decreasing = True, True
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                decreasing = False
            if nums[i] < nums[i - 1]:
                increasing = False
        return decreasing or increasing

    # Time complexity: O(n)
    # Space complexity: O(1)
    def isMonotonic3(self, nums: list[int]) -> bool:
        increasing, decreasing = True, True
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                decreasing = False
            if nums[i] < nums[i - 1]:
                increasing = False
            if not increasing and not decreasing:
                return False
        return True
