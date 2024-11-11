class Solution:
    # Time complexity: O(n! * n^2)
    # If we have 3 elements, then we have 3 * 2 * 1 permutations.
    # For each of the permutation we have to insert (O(n)).
    # We insert n elements into each permutation, therefore (O(n^2))
    # But the dominant factor here is still the n!.
    # So we can think of the time complexity as O(n!).
    # The key identifier for n! complexity is when you need to generate all possible orderings/arrangements of elements.
    # Space complexity: O(n) - recursion depth
    # Since we store all permutations
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 0:
            return [[]]

        permutations = self.permute(nums[1:])

        res = []
        for p in permutations:
            # Insert current_num in each gap in p
            for i in range(len(p) + 1):  # +1 because we can also insert at the end
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res

    # Complexity: same as above
    def permute_iterative(self, nums: list[int]) -> list[list[int]]:
        permutations = [[]]
        for n in nums:
            new_permutations = []
            for p in permutations:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_permutations.append(p_copy)
            permutations = new_permutations
        return permutations

    # Time complexity: O(n!)
    # Space complexity: O(n)
    def permute2(self, nums: list[int]) -> list[list[int]]:
        res, curr = [], []

        def backtrack():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for n in nums:
                if n not in curr:
                    curr.append(n)
                    backtrack()
                    curr.pop()

        backtrack()
        return res
