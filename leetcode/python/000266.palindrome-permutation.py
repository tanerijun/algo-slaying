from collections import Counter


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1) -> max(26)
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        odd_count = 0
        for v in counter.values():
            if v % 2 == 1:
                odd_count += 1
            if odd_count > 1:
                return False
        return True
