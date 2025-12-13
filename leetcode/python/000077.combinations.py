class Solution:
    # Time complexity: O(k * C(n, k))
    # Space complexity: O(k)
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        temp = []

        def dfs(starting_n):
            if len(temp) == k:
                res.append(temp.copy())
                return

            for i in range(starting_n, n + 1):
                temp.append(i)
                dfs(i + 1)
                temp.pop()

        dfs(1)
        return res
