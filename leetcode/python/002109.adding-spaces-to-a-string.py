class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        spaces_idx = 0
        res = []
        for i in range(len(s)):
            if spaces_idx < len(spaces) and i == spaces[spaces_idx]:
                res.append(" ")
                spaces_idx += 1
            res.append(s[i])
        return "".join(res)
