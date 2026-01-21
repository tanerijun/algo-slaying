class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    def specialArray(self, nums: list[int]) -> int:
        for x in range(1, len(nums) + 1):
            count = 0
            for n in nums:
                if n >= x:
                    count += 1
            if count == x:
                return x
        return -1

    # Time complexity: O(n(log(n)))
    # Space complexity: O(1)
    def specialArray1(self, nums: list[int]) -> int:
        left, right = 1, len(nums) + 1

        while left <= right:
            mid = (left + right) // 2

            count = 0
            for n in nums:
                if n >= mid:
                    count += 1

            if count == mid:
                return mid

            if count < mid:
                right = mid - 1
            else:
                left = mid + 1

        return -1
