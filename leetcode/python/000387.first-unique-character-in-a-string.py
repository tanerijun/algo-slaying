from collections import Counter


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1) -> max 26
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
        return -1
