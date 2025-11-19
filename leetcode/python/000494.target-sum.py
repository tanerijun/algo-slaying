from collections import defaultdict


class Solution:
    # Time complexity: O(2^n)
    # Space complexity: O(n)
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        def dfs(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            return dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])

        return dfs(0, 0)

    # Time complexity: O(n * s) where n is the number of elements in nums and s is the sum of elements in nums
    # Space complexity: O(n * s)
    def findTargetSumWays2(self, nums: list[int], target: int) -> int:
        # key => tuple (i, total) representing (current_index, current_sum)
        # value => number of ways to reach the target from this state
        cache = {}

        # i: The current index of the number we are considering in the 'nums' array.
        # total: The current accumulated sum.
        def dfs(i, total):
            if (i, total) in cache:
                return cache[(i, total)]

            if i == len(nums):
                return 1 if total == target else 0

            # Recursive Step: Explore two possibilities for the current number nums[i]:
            #
            # 1. Add the current number (dfs(i + 1, total + nums[i])):
            #    We assign a '+' sign to nums[i] and add it to the current total.
            #    Then, we move to the next number (i + 1).
            #
            # 2. Subtract the current number (dfs(i + 1, total - nums[i])):
            #    We assign a '-' sign to nums[i] and subtract it from the current total.
            #    Then, we move to the next number (i + 1).
            #
            # The total number of ways for the current subproblem (i, total) is the
            # sum of the ways from these two branches.
            cache[(i, total)] = dfs(i + 1, total + nums[i]) + dfs(
                i + 1, total - nums[i]
            )
            return cache[(i, total)]

        return dfs(0, 0)

    # Time complexity: O(n * s) where n is the number of elements and s is the total sum
    # Space complexity: O(n * s)
    def findTargetSumWays3(self, nums: list[int], target: int) -> int:
        """
        This bottom-up approach transforms the problem into a subset sum problem.

        ### The Idea: The "Two Piles" Analogy
        Imagine partitioning the `nums` array into two subsets:
        - A "Plus Pile" (P), where we assign a '+' sign to each number.
        - A "Minus Pile" (N), where we assign a '-' sign to each number.

        The goal is to find the number of ways such that:
        `sum(P) - sum(N) = target`

        We also know that the sum of all numbers in both piles is the total sum of the array:
        `sum(P) + sum(N) = total_sum`

        ### The Mathematical Transformation
        By adding these two equations together, we can eliminate `sum(N)`:
        `(sum(P) - sum(N)) + (sum(P) + sum(N)) = target + total_sum`
        `2 * sum(P) = target + total_sum`
        `sum(P) = (target + total_sum) / 2`

        This gives us a new, simpler problem:
        "Find the number of subsets of `nums` that sum up to `(target + total_sum) / 2`."

        This is a subset sum problem, which can be solved efficiently with dynamic programming.

        ### Dynamic Programming Approach
        We use a 2D DP table to solve the subset sum problem.
        - **State:** `dp[i][j]` = the number of ways to form a sum of `j` using the first `i` numbers.
        - **Recurrence Relation:** For each number `num = nums[i-1]` and each sum `j`:
            - **Don't include `num`:** The number of ways is `dp[i-1][j]`.
            - **Include `num`:** The number of ways is `dp[i-1][j - num]` (only if `j >= num`).
            - **Total:** `dp[i][j] = dp[i-1][j] + dp[i-1][j - num]`.
        - **Base Case:** `dp[0][0] = 1` (There is one way to make a sum of 0 with no numbers: the empty set).
        """
        total_sum = sum(nums)

        # If the target is unreachable or the subset sum is not an integer,
        # it's impossible to find a solution.
        if abs(target) > total_sum or (target + total_sum) % 2 != 0:
            return 0

        # The problem is now to find the number of subsets that sum up to this value.
        subset_sum = (target + total_sum) // 2

        # dp[i][j] = number of ways to get sum 'j' using the first 'i' numbers.
        # Rows: 'len(nums) + 1' for each number plus the base case of no numbers.
        # Columns: 'subset_sum + 1' for sums from 0 to 'subset_sum'.
        dp = [[0] * (subset_sum + 1) for _ in range(len(nums) + 1)]

        # Base case: There is one way to make a sum of 0 with no elements (the empty set).
        dp[0][0] = 1

        # Iterate through each number in nums. 'i' corresponds to using the first 'i' numbers.
        for i in range(1, len(nums) + 1):
            # The current number we are considering is nums[i-1].
            num = nums[i - 1]
            # Iterate through all possible target sums from 0 to subset_sum.
            for j in range(subset_sum + 1):
                # Option 1: Don't include the current number (num).
                # The number of ways to form sum 'j' is the same as it was
                # with the previous 'i-1' numbers.
                dp[i][j] = dp[i - 1][j]

                # Option 2: Include the current number (num).
                # This is only possible if the current sum 'j' is greater than
                # or equal to the number's value.
                if j >= num:
                    # Add the number of ways to form the remaining sum (j - num)
                    # using the previous 'i-1' numbers.
                    dp[i][j] += dp[i - 1][j - num]

        # The final answer is in dp[len(nums)][subset_sum].
        # This represents the number of ways to make the 'subset_sum'
        # using all available numbers in 'nums'.
        return dp[len(nums)][subset_sum]

    # Time complexity: O(n * s)
    # Space complexity: O(s)
    def findTargetSumWays4(self, nums: list[int], target: int) -> int:
        """
        This is a space-optimized version of the bottom-up DP approach.

        ### The Logic for Space Optimization
        In the 2D DP approach, we noticed that the calculation for the current row `dp[i]`
        only depends on the values from the previous row `dp[i-1]`. This means we don't
        need to store the entire 2D table. We can use a single 1D array to store the
        results of the previous state.

        Let `dp[j]` be the number of ways to form a sum of `j`.
        We iterate through each number `num` in `nums` and update this `dp` array.

        ### The Iteration Order is Key
        The update rule is `dp[j] = dp[j] (without num) + dp[j - num] (with num)`.

        If we iterate `j` from left to right (from 0 to `subset_sum`), when we calculate
        `dp[j]`, the value `dp[j - num]` would have already been updated in the same loop
        for the current `num`. This is incorrect as it would be like using the same
        number multiple times for a single state transition.

        To use the values from the *previous* state (before considering the current `num`),
        we must iterate `j` backwards, from `subset_sum` down to `num`. This ensures that
        `dp[j - num]` still holds the value from the previous outer loop iteration.
        """
        total_sum = sum(nums)

        if abs(target) > total_sum or (target + total_sum) % 2 != 0:
            return 0

        subset_sum = (target + total_sum) // 2

        # dp[j] will store the number of ways to make sum j.
        dp = [0] * (subset_sum + 1)

        # Base case: There is one way to make a sum of 0 (by using no numbers).
        dp[0] = 1

        # Iterate through each number in the input array.
        for num in nums:
            # Iterate backwards to prevent using the same element multiple times in one subset.
            for j in range(subset_sum, num - 1, -1):
                # For each number, we can either include it or not.
                # dp[j] is the count of ways without including the number.
                # dp[j - num] is the count of ways from the previous state for the remaining sum.
                dp[j] += dp[j - num]

        # The final answer is the number of ways to form the 'subset_sum'.
        return dp[subset_sum]

    # Time complexity: O(n * s)
    # Space complexity: O(n * s)
    def findTargetSumWays5(self, nums: list[int], target: int) -> int:
        """
        This approach directly simulates the process of building the sum without the
        mathematical transformation used in the subset sum method. It is often more intuitive.

        - **State:** `dp[i][j]` = the number of ways to achieve a sum of `j` using the first `i` numbers.
            We use a list of dictionaries, where each dictionary stores the possible sums and their counts.
        - **Base Case:** `dp[0][0] = 1`, meaning with zero numbers, there's one way to make a sum of 0.
        - **Recurrence:** For each number `num = nums[i]`, we look at all the sums `total` achievable with
            the first `i` numbers. For each `total` achieved in `count` ways, we can now form two new sums
            with the `(i+1)`-th number: `total + num` and `total - num`.
        """
        n = len(nums)
        # dp[i] is a dictionary mapping a sum to the number of ways to achieve it
        # using the first i numbers.
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(n):
            num = nums[i]
            # For each sum 'total' achievable with the first 'i' numbers...
            for total, count in dp[i].items():
                # We can now form two new sums with the (i+1)-th number.
                dp[i + 1][total + num] += count
                dp[i + 1][total - num] += count

        # The final answer is the number of ways to get the target sum using all n numbers.
        return dp[n][target]

    # Time complexity: O(n * s)
    # Space complexity: O(s)
    def findTargetSumWays6(self, nums: list[int], target: int) -> int:
        """
        This is the space-optimized version of findTargetSumWays5.
        Instead of keeping a DP table for each of the `n` steps, we only need to store
        the results from the previous step to compute the results for the current step.

        We use one dictionary `dp` to store the sums achievable at the current step.
        In each iteration, we create a new dictionary `next_dp` to build the next state
        based on the current `dp` and the current number, and then replace `dp` with `next_dp`.
        """
        # Base case: Before processing any numbers, there's one way to get a sum of 0.
        dp = defaultdict(int)
        dp[0] = 1

        # Iterate through each number.
        for num in nums:
            # Create a new dictionary to store the results of the current step.
            next_dp = defaultdict(int)
            # For each sum 'total' achievable in the previous step...
            for total, count in dp.items():
                # Calculate the new possible sums and add the counts.
                next_dp[total + num] += count
                next_dp[total - num] += count
            # The next state becomes our current state for the next number.
            dp = next_dp

        # The final dictionary holds the counts for all possible sums using all numbers.
        return dp[target]
