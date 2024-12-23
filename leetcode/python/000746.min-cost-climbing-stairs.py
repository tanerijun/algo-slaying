class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost.append(0)  # the top is 0 (no cost)

        # The cost for the last step to reach the top is guaranteed to be itself
        for i in range(len(cost) - 3, -1, -1):
            cost[i] = cost[i] + min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])

    # Time complexity: O(n)
    # Space complexity: O(1)
    def minCostClimbingStairs2(self, cost: list[int]) -> int:
        one, two = cost[len(cost) - 1], 0

        for i in range(len(cost) - 2, -1, -1):
            temp = cost[i] + min(one, two)
            two = one
            one = temp

        return min(one, two)
