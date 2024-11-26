class Solution:
    # Time complexity: O(2^n * n)
    # Space complexity: O(n) - recursion and temp; O(2^n) if including res
    def partition(self, s: str) -> list[list[str]]:
        res, temp = [], []

        def dfs(i):
            if i == len(s):
                res.append(temp.copy())
                return

            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]: # check if palindrome
                    temp.append(s[i:j+1])
                    dfs(j + 1)
                    temp.pop()

        dfs(0)
        return res
