class Solution:
    # Time complexity: O(2^n)
    # Space complexity: O(n)
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        def dfs(idx, container):
            if idx == len(nums):
                res.append(container.copy())  # a new reference
                return

            # include current number
            container.append(nums[idx])
            dfs(idx + 1, container)

            # exclude current number
            container.pop()
            dfs(idx + 1, container)

        dfs(0, [])
        return res
