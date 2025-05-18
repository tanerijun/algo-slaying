class Solution:
    # Time complexity: O(n)
    # Space complexity: O(m) - m is the total number of unique chars in the string
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

    # Time complexity: O(n)
    # Space complexity: O(m) - m is the total number of unique chars in the string
    def characterReplacementOptimized(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        max_freq = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_freq = max(max_freq, count[s[r]])

            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
