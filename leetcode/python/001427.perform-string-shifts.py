class Solution:
    # Time complexity: O(n) -> length of shift
    # Space complexity: O(l) -> length of string (string creation cost)
    def stringShift(self, s: str, shift: list[list[int]]) -> str:
        x = 0
        for shf in shift:
            x += shf[1] * (-1 if shf[0] == 0 else 1)

        x = x % len(s)  # handle cases where |x| > len(s)
        return s[-x:] + s[:-x] if x != 0 else s
