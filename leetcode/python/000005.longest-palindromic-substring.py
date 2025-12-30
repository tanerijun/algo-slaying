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

    # Time complexity: O(n2)
    # Space complexity: O(1)
    def longestPalindrome2(self, s: str) -> str:
        def expand_around_center(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r

        start, end = 0, 0
        for i in range(len(s)):
            l1, r1 = expand_around_center(i, i)
            l2, r2 = expand_around_center(i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end]
