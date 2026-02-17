class Solution:
    # Time complexity: O(log(n))
    # Space complexity: O(1)
    def findKthPositive(self, arr: list[int], k: int) -> int:
        l, r = 0, len(arr) - 1

        while l <= r:
            m = (l + r) // 2
            # -1 because number starts from 1
            # intuition for -m:
            # assume there is no missing number up to m = 3 -> 1, 2, 3
            #   missing_positives = 3 - 1 - 2 = 0 (no missing)
            # but if we have missing number: 1, 3
            #   missing_positives = 3 - 1 - 1 = 1 (1 number missing, number 2)
            missing_positives = arr[m] - 1 - m

            if missing_positives >= k:
                r = m - 1
            else:
                l = m + 1

        # At this point, pointer R comes before L, with L being R + 1.
        # And the answer lives somewhere between R and L.
        missing_positives = arr[r] - 1 - r
        return arr[r] + (k - missing_positives)
