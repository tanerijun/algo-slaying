class Solution:
    # Time complexity: O(len(s))
    # Space complexity: O(1)
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1

        return 0 if j == len(t) else len(t) - j
