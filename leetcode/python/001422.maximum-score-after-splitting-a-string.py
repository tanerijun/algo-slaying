class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def maxScore(self, s: str) -> int:
        ones = s.count("1")
        zeros = 0
        res = 0

        for i in range(len(s) - 1):
            if s[i] == "1":
                ones -= 1
            else:
                zeros += 1

            res = max(res, zeros + ones)

        return res
