class Solution:
    # Time complexity: O(m * n)
    # Space complexity: O(1)
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        firstRowZero, firstColZero = False, False

        for i in range(n):
            if matrix[0][i] == 0:
                firstRowZero = True

        for i in range(m):
            if matrix[i][0] == 0:
                firstColZero = True

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if firstRowZero:
            for i in range(n):
                matrix[0][i] = 0

        if firstColZero:
            for i in range(m):
                matrix[i][0] = 0
