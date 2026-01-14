class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def largestGoodInteger(self, num: str) -> str:
        good_int = -1
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                good_int = max(good_int, int(num[i]))
        return str(good_int) * 3 if good_int >= 0 else ""

    # Time complexity: O(n)
    # Space complexity: O(1)
    def largestGoodInteger2(self, num: str) -> str:
        for i in range(9, -1, -1):
            substr = str(i) * 3
            if substr in num:
                return substr
        return ""
