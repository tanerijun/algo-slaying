class Solution:
    # Time complexity: O(n). Solve this problem bottom-up (fibonacci)
    # Space complexity: O(1)
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for _ in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one
