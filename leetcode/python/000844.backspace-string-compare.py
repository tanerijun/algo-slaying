class Solution:
    # Time complexity: O(n + m)
    # Space complexity: O(1)
    def backspaceCompare(self, s: str, t: str) -> bool:
        def next_valid_index(string, i):
            skip = 0
            while i >= 0:
                if string[i] == "#":
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    return i
                i -= 1
            return -1

        i, j = len(s) - 1, len(t) - 1

        while True:
            i = next_valid_index(s, i)
            j = next_valid_index(t, j)

            if i < 0 and j < 0:
                return True
            if i < 0 or j < 0:
                return False
            if s[i] != t[j]:
                return False

            i -= 1
            j -= 1
