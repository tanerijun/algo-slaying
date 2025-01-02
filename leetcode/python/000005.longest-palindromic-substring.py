class Solution:
    # Time complexity: O(n2)
    # Space complexity: O(1)
    def longestPalindrome(self, s: str) -> str:
        resStartIndex = 0
        currentMaxLen = 0

        for i in range(len(s)):
            l, r = i, i  # when len(s) is odd

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            length = r - l - 1
            if length > currentMaxLen:
                resStartIndex = l + 1
                currentMaxLen = length

            l, r = i, i + 1  # when len(s) is even
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            length = r - l - 1
            if length > currentMaxLen:
                resStartIndex = l + 1
                currentMaxLen = length

        return s[resStartIndex : resStartIndex + currentMaxLen]
