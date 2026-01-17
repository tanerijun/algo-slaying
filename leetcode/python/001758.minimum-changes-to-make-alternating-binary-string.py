class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def minOperations(self, s: str) -> int:
        start0 = "0"  # if s starts with 0
        start1 = "1"  # if s starts with 1
        needed0 = 0  # changes needed using start0
        needed1 = 0  # changes needed using start1

        for ch in s:
            if ch != start0:
                needed0 += 1
            if ch != start1:
                needed1 += 1
            start0 = "0" if start0 == "1" else "1"
            start1 = "0" if start1 == "1" else "1"

        return min(needed0, needed1)
