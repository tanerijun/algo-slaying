class Solution:
    # Time complexity: O(n * 2^n)
    # - Include, exclude, and copying container
    # Space complexity: O(n)
    # - Res is part of output space, so it's not counted here
    # - The space complexity is O(n) because of recursion
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
