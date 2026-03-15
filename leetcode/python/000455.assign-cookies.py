class Solution:
    # Time complexity: O(n(log(n)) + m(log(m)))
    # Space complexity: O(n + m) - from sorting algorithm
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if s[j] < g[i]:
                j += 1
            else:
                i += 1
                j += 1
        return i
