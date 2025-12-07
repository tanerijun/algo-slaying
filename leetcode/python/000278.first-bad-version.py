# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# Mock implementation
def isBadVersion(version: int) -> bool:
    return False


class Solution:
    # Time complexity: O(log(n))
    # Space complexity: O(1)
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        ans = 0
        while l <= r:
            m = (l + r) // 2
            if isBadVersion(m):
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans
