class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Find the median of two sorted arrays using binary search.

        APPROACH: Instead of merging arrays (O(m+n)), we use binary search to find
        the correct partition point that divides both arrays into left/right halves.

        For a valid partition:
        - All elements in left half ≤ all elements in right half
        - Left half has same size as right half (or 1 more if odd total length)

        Time Complexity: O(log(min(m, n)))
        Space Complexity: O(1)
        """

        # OPTIMIZATION: Always binary search on the smaller array to minimize iterations
        # This ensures our search space is log(min(m,n))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # l, r represent how many elements we take from nums1 for the left partition
        l, r = 0, len(nums1)

        while True:
            # PARTITION INDEX for nums1:
            # i represents the last index we include from nums1 in the left partition
            # So we're taking elements nums1[0] through nums1[i] (i+1 elements total)
            i = (l + r) // 2

            # PARTITION INDEX for nums2:
            # We need to determine j such that left and right partitions are balanced
            #
            # Goal: (i+1) + (j+1) = (len(nums1) + len(nums2)) // 2
            #         ↑       ↑                ↑
            #      elements elements      total elements
            #      from     from          in left partition
            #      nums1    nums2
            #
            # Solving for j:
            #   i + 1 + j + 1 = (len(nums1) + len(nums2)) // 2
            #   j + 2 = (len(nums1) + len(nums2)) // 2 - i
            #   j = (len(nums1) + len(nums2)) // 2 - i - 2
            j = (len(nums1) + len(nums2)) // 2 - i - 2

            # GET BOUNDARY ELEMENTS:
            # We need to check if our partition is valid by comparing:
            # - The largest element in the left partition
            # - The smallest element in the right partition

            # nums1Left: largest element from nums1 in left partition
            # If i < 0, we're not taking any elements from nums1, use -infinity
            nums1Left = nums1[i] if i >= 0 else float("-inf")

            # nums2Left: largest element from nums2 in left partition
            # If j < 0, we're not taking any elements from nums2, use -infinity
            # (This CAN happen when i is large)
            nums2Left = nums2[j] if j >= 0 else float("-inf")

            # nums1Right: smallest element from nums1 in right partition
            # If i+1 >= len(nums1), all nums1 elements are in left, use +infinity
            nums1Right = nums1[i + 1] if i + 1 < len(nums1) else float("inf")

            # nums2Right: smallest element from nums2 in right partition
            # If j+1 >= len(nums2), all nums2 elements are in left, use +infinity
            nums2Right = nums2[j + 1] if j + 1 < len(nums2) else float("inf")

            # CHECK IF PARTITION IS VALID:
            # A valid partition means:
            # - max(left partition) ≤ min(right partition)
            # - Specifically: nums1Left ≤ nums2Right AND nums2Left ≤ nums1Right
            #
            # Why both conditions? Because the max of left could come from either array,
            # and the min of right could come from either array.
            if nums1Left <= nums2Right and nums2Left <= nums1Right:
                # FOUND THE CORRECT PARTITION! Calculate median:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    # EVEN total length: median is average of two middle elements
                    # - max(nums1Left, nums2Left) is the largest in left partition
                    # - min(nums1Right, nums2Right) is the smallest in right partition
                    # These are the two middle elements
                    return (max(nums1Left, nums2Left) + min(nums1Right, nums2Right)) / 2
                else:
                    # ODD total length: median is the smallest element in right partition
                    # When total is odd, integer division (// 2) naturally puts fewer
                    # elements in left, so right partition has 1 more element.
                    # The median is the smallest element in the larger (right) partition.
                    return min(nums1Right, nums2Right)

            # PARTITION IS INVALID - ADJUST BINARY SEARCH:
            else:
                if nums1Left > nums2Right:
                    # nums1Left is too large!
                    # We took too many elements from nums1 for the left partition
                    # Move partition point LEFT (decrease i)
                    r = i - 1
                else:
                    # nums2Left > nums1Right
                    # We took too few elements from nums1 for the left partition
                    # (equivalently: too many from nums2)
                    # Move partition point RIGHT (increase i)
                    l = i + 1
