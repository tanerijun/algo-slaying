class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """

    # Time complexity: O(n)
    # Space complexity: O(1)
    def is_strobogrammatic(self, num: str) -> bool:
        m = {"0": "0", "1": "1", "6": "9", "9": "6", "8": "8"}

        l, r = 0, len(num) - 1
        while l <= r:
            if num[l] not in m or num[r] not in m:
                return False
            if m[num[l]] != num[r] or m[num[r]] != num[l]:
                return False
            l += 1
            r -= 1

        return True
