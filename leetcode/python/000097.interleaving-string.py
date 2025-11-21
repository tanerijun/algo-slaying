class Solution:
    # Time complexity: O(m * n)
    # Space complexity: O(m * n)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        # Key: A tuple (i, j) representing the current indices in s1 and s2.
        # Value: A boolean indicating whether s3[i+j:] can be formed by interleaving s1[i:] and s2[j:].
        cache = {}

        def dfs(i, j):
            # If we have exhausted both s1 and s2, it means s3 has been successfully
            # formed by interleaving s1 and s2 up to this point.
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in cache:
                return cache[(i, j)]
            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True
            cache[(i, j)] = False
            return False

        return dfs(0, 0)

    # Time complexity: O(m * n)
    # Space complexity: O(m * n)
    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        # dp[i][j] will represent if s1[:i] and s2[:j] can form s3[:i+j]
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True

        return dp[0][0]

    # Time complexity: O(m * n)
    # Space complexity: O(min(m, n))
    # This solution optimizes space from O(m*n) to O(max(m, n)) by using only two "rows"
    def isInterleave3(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        # Optimization: Ensure s1 is the shorter string.
        # This makes 'm' (length of s1) min(original_lens) and 'n' (length of s2) max(original_lens).
        # The DP array will have size 'n+1', so space complexity becomes O(n) or O(max(original_lens)).
        if len(s1) > len(s2):
            s1, s2 = s2, s1

        m, n = len(s1), len(s2)

        # `dp` array represents a single "row" of the 2D DP table (for s2 indices).
        # Specifically, `dp[j]` stores whether s3[i+1+j:] can be formed by interleaving
        # s1[i+1:] and s2[j:] for the (i+1)th row (the row below the current 'i' being calculated).
        dp = [False] * (n + 1)

        # Base case initialization: dp[m][n] = True. When s1 and s2 are both exhausted, s3 is also exhausted.
        # This initial setting corresponds to dp[m][n] in the conceptual 2D table.
        # It's used as the base for filling the `m`th row (when i=m) and subsequently other rows.
        dp[n] = True

        # Outer loop iterates 'i' (index for s1) from m down to 0.
        # Each iteration calculates a new "row" of the DP table (for current 'i').
        for i in range(m, -1, -1):
            # `next_dp` will store the results for the current row 'i' (dp[i][:]).
            # This is effectively dp[i][j] where 'j' is the inner loop index.
            next_dp = [False] * (n + 1)

            # Special handling for the cell dp[i][n].
            # When i=m (s1 exhausted), dp[m][n] should be True.
            # This line ensures `next_dp[n]` is correctly set to `True` for the 'm'th row.
            # For `i < m`, `next_dp[n]` (which is `dp[i][n]`) will depend on `s1[i]` and `dp[i+1][n]`,
            # which is handled by the first `if` condition in the inner loop.
            if i == m:
                next_dp[n] = True

            # Inner loop iterates 'j' (index for s2) from n down to 0.
            # This fills the `next_dp` array (representing the current row 'i') from right to left.
            for j in range(n, -1, -1):
                # Option 1: Check if s1[i] can be the current character in s3.
                # If s1[i] is in bounds (`i < m`), matches `s3[i+j]`, AND the rest of `s1[i+1:]` and `s2[j:]`
                # can form `s3[i+j+1:]`.
                # `dp[j]` here corresponds to `dp[i+1][j]` from the 2D DP table (the value from the row below).
                if i < m and s1[i] == s3[i + j] and dp[j]:
                    next_dp[j] = True

                # Option 2: Check if s2[j] can be the current character in s3.
                # This condition is evaluated after Option 1, allowing for `next_dp[j]` to be set by either path.
                # If `s2[j]` is in bounds (`j < n`), matches `s3[i+j]`, AND the rest of `s1[i:]` and `s2[j+1:]`
                # can form `s3[i+j+1:]`.
                # `next_dp[j+1]` here corresponds to `dp[i][j+1]` from the 2D DP table (the element to the right
                # in the current row `i`, which has already been computed because `j` is decreasing).
                if j < n and s2[j] == s3[i + j] and next_dp[j + 1]:
                    next_dp[j] = True
            dp = next_dp

        return dp[0]
