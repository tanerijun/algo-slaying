class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.countPalindrome(s, i, i)
            res += self.countPalindrome(s, i, i + 1)

        return res

    def countPalindrome(self, s: str, l: int, r: int) -> int:
        res = 0

        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1

        return res
