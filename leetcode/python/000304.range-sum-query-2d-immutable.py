# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


class NumMatrix:
    # Time complexity: O(m * n)
    # Space complexity: O(m * n)
    def __init__(self, matrix: list[list[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefix_sum = []
        for r in range(rows):
            self.prefix_sum.append([])
            cur_sum = 0
            for c in range(cols):
                cur_sum += matrix[r][c]
                self.prefix_sum[r].append(
                    cur_sum + (self.prefix_sum[r - 1][c] if r > 0 else 0)
                )

    # Time complexity: O(1)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_total = self.prefix_sum[row2][col2]
        sum_top = self.prefix_sum[row1 - 1][col2] if row1 > 0 else 0
        sum_left = self.prefix_sum[row2][col1 - 1] if col1 > 0 else 0
        # Need to add back sum_top_left because it's subtracted twice since it's included
        # both in sum_top and sum_left
        sum_top_left = (
            self.prefix_sum[row1 - 1][col1 - 1] if (row1 > 0 and col1 > 0) else 0
        )
        return sum_total - sum_top - sum_left + sum_top_left
