class Solution:
    # Time complexity: O(2^T), T = target, Or more specifically O(2^(T/(min(candidates))))
    # Space complexity: O(T)
    # The time complexity is O(2^t) where t is the target value, because at each recursive call we have two choices:
    # either use the current number again (staying at the same index) or skip it (moving to next index).
    # Unlike typical subset problems where we just move to the next index, here we can reuse numbers,
    # so our recursive tree's depth is bounded by the target value rather than array length.
    # We keep making recursive calls until we either reach the target sum or exceed it.
    # Each path in our recursion can use a number multiple times until the sum exceeds target,
    # so our branching continues until we hit target or go over.
    # For space complexity, it's O(target) since our recursion depth is bounded by the target value,
    # as we can't make more recursive calls than the target itself without exceeding it."
    # This problem is like making change: you can reuse coins (staying at same index) or move to next coin (index + 1), and you keep going until you hit or exceed your target amount.
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
