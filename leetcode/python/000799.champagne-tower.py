class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(n)
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prev = [poured]  # flow (can be greater than 1)

        # Skip 1 iteration since we already have initialized with first row
        for row in range(1, query_row + 1):
            cur = [0.0] * ((row) + 1)  # each row has (row + 1) glasses
            for i in range(row):
                extra = prev[i] - 1
                if extra > 0:
                    cur[i] += extra * 0.5
                    cur[i + 1] += extra * 0.5
            prev = cur

        # Since the array contains flow, not liquid quantity
        return min(1, prev[query_glass])

    # Same as above, but with different variable names
    def champagneTower2(self, poured: int, query_row: int, query_glass: int) -> float:
        prev = [poured]

        for _ in range(query_row):
            cur = [0.0] * (len(prev) + 1)
            for i in range(len(prev)):
                extra = prev[i] - 1
                if extra > 0:
                    cur[i] += extra * 0.5
                    cur[i + 1] += extra * 0.5
            prev = cur

        return min(1, prev[query_glass])

    # Example: poured = 4, query_row = 2, query_glass = 1
    # Initial:
    #   prev = [4]
    # Iteration 1 (row 1):
    #   cur = [0.0, 0.0]
    #   i = 0:
    #       extra = 4 - 1 = 3
    #       cur[0] += 3 * 0.5 = 1.5
    #       cur[1] += 3 * 0.5 = 1.5
    #   prev = [1.5, 1.5]
    # Iteration 2 (row 2):
    #   cur = [0.0, 0.0, 0.0]
    #   i = 0:
    #       extra = 1.5 - 1 = 0.5
    #       cur[0] += 0.5 * 0.5 = 0.25
    #       cur[1] += 0.5 * 0.5 = 0.25
    #   i = 1:
    #       extra = 1.5 - 1 = 0.5
    #       cur[1] += 0.5 * 0.5 = 0.25  # cur[1] is now 0.5
    #       cur[2] += 0.5 * 0.5 = 0.25
    #   prev = [0.25, 0.5, 0.25]
