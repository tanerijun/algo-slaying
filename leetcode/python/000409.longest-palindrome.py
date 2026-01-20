from collections import Counter


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1) -> max 26
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        res = 0
        added_orphan = False  # each palindrome can only has at most 1 orphan

        for v in counter.values():
            if v % 2 == 0:
                res += v
            else:
                res += v - 1  # odd count, add the evens
                if not added_orphan:
                    res += 1
                    added_orphan = True

        return res
