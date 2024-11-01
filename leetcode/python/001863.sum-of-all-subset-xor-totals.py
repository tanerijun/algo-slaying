class Solution:
    # Time complexity: O(n * 2^n)
    # - Each element can be included or excluded from any given subset, meaning there are 2^n possible subsets. (O(2^n))
    # - We iterate through each subsets to calculate the result. The average size of each subset is approximately n/2. (O(n/2 * 2^n))
    # Space complexity: O(n * 2^n)
    # - The subsets list will contain 2^n subsets with average size of n/2. (O(n/2 * 2^n))
    # - The recursion depth can reach size n. (O((n + n/2) * 2^n))
    def subsetXORSum(self, nums: list[int]) -> int:
        xor_total = 0

        def dfs(index, container):
            if index == len(nums):
                nonlocal xor_total
                xor = 0
                for i in container:
                    xor ^= nums[i]
                xor_total += xor
                return

            container.append(index)
            dfs(index + 1, container)

            container.pop()
            dfs(index + 1, container)

        dfs(0, [])
        return xor_total

    # Intuition: Doing the XOR calculation on the fly
    # For the current subset, we save the XOR total by adding the element to the subset in the variable withElement
    # and the XOR total by not adding the element in the variable withoutElement.
    # Each of these variables represents the XOR total of a different subset,
    # so we can return their sum to compute the running total for those two subsets.
    # Time complexity: O(2^n)
    # - We traverse through each of the 2^n subset to calculate result
    # Space complexity: O(n)
    # - The recursion depth can reach n
    def subsetXORSumOptimizedBacktracking(self, nums: list[int]) -> int:
        def generate_subsets(nums: list[int], index: int, current_XOR: int) -> int:
            # Return current_XOR when all elements in nums are already considered
            if index == len(nums):
                return current_XOR

            # Calculate sum of subset xor with current element
            with_element = generate_subsets(nums, index + 1, current_XOR ^ nums[index])

            # Calculate sum of subset xor without current element
            without_element = generate_subsets(nums, index + 1, current_XOR)

            return with_element + without_element

        return generate_subsets(nums, 0, 0)
