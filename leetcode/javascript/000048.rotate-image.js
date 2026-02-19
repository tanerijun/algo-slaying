/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 * Algorithm: Transpose matrix, then reverse each row
 * Time complexity: O(n^2)
 * Space complexity: O(1)
 */
var rotate = function (matrix) {
  // Transpose (turn rows to columns)
  for (let i = 0; i < matrix.length; i++) {
    for (let j = i; j < matrix.length; j++) {
      [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
    }
  }

  // Reverse row
  for (const row of matrix) {
    for (let i = 0; i < row.length / 2; i++) {
      [row[i], row[row.length - 1 - i]] = [row[row.length - 1 - i], row[i]];
    }
  }

  // Or using built-in
  // for (const row of matrix) {
  //   row.reverse();
  // }

  return matrix;
};
