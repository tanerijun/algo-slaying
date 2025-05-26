class Solution:
    # Time complexity: O(log(n))
    # Space complexity: O(log(n))
    def isHappy(self, n: int) -> bool:
        visit = set()

        def sum_of_squares(n):
            res = 0
            while n > 0:
                res += (n % 10) ** 2
                n //= 10
            return res

        while n not in visit:
            visit.add(n)

            n = sum_of_squares(n)

            if n == 1:
                return True

        return False

    # Time complexity: O(log(n))
    # Space complexity: O(1)
    def isHappy2(self, n: int) -> bool:
        def sum_of_squares(n):
            res = 0
            while n > 0:
                res += (n % 10) ** 2
                n //= 10
            return res

        slow, fast = n, sum_of_squares(n)

        while slow != fast:
            fast = sum_of_squares(fast)
            fast = sum_of_squares(fast)
            slow = sum_of_squares(slow)

        return True if fast == 1 else False
