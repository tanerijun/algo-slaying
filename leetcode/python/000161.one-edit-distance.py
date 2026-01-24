class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # Ensure s is the shorter string, so that we can avoid considering deletion
        if len(t) < len(s):
            return self.isOneEditDistance(t, s)

        if len(t) - len(s) > 1:
            return False

        for i in range(len(s)):
            if s[i] != t[i]:
                if len(s) == len(t):
                    return s[i + 1 :] == t[i + 1 :]  # replace then check the rest
                else:
                    return s[i:] == t[i + 1 :]  # insert then check the rest

        # If there are no diffs in len(s) distance
        # The strings are one dit away only if t has 1 more char
        return len(t) == len(s) + 1
