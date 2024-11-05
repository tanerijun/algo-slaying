class Solution:
    # Time complexity: O(2^T), T = target
    # We make 2 decisions each time, and the tree height is at most T
    # Space complexity: O(n)
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            # Include the value at i
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            # Exclude the value at i
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
