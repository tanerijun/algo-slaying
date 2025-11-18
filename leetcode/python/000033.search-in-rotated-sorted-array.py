class Solution:
    # Time complexity: O(log(n))
    # Space complexity: O(1)
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # Determine which half is sorted.
            # Case 1: The left half (from l to m) is sorted.
            # This happens if nums[l] is less than or equal to nums[m].
            # Example: [4, 5, 6, 7, 0, 1, 2], l=0, m=3, nums[l]=4, nums[m]=7. Left half [4,5,6,7] is sorted.
            # Example: [0, 1, 2, 4, 5, 6, 7], l=0, m=3, nums[l]=0, nums[m]=4. Left half [0,1,2,4] is sorted.
            if nums[l] <= nums[m]:
                # Check if the target is within the sorted left half.
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    # Target is not in the left sorted half, so it must be in the right (potentially unsorted) half.
                    l = m + 1

            # Case 2: The right half (from m to r) is sorted.
            # This happens if nums[l] is greater than nums[m], indicating the rotation
            # point is in the left half, and the right half is continuous and sorted.
            # Example: [6, 7, 0, 1, 2, 3, 4, 5], l=0, m=3, nums[l]=6, nums[m]=1. Left half [6,7,0,1] is not sorted.
            # Therefore, the right half [1,2,3,4,5] (from m to r) must be sorted.
            else:  # nums[l] > nums[m]:
                # Check if the target is within the sorted right half.
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1
