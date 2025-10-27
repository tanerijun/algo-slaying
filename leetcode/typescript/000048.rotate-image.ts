/**
 * Time complexity: O(n^2)
 * Space complexity: O(1)
 * Algorithm:
 * - Rotate the matrix in place layer by layer (outer to inner).
 * - For each element on the top edge (i, j) of a layer, perform a 4-way swap.
 * - For a 90° clockwise rotation, each coordinate (r, c) maps to (c, n - 1 - r).
 *   Applying this yields the 4 corresponding positions:
 *     top    (i, j)                  -- start of the cycle
 *     right  (j, n - 1 - i)          -- from rotation formula
 *     bottom (n - 1 - i, n - 1 - j)  -- rotate again
 *     left   (n - 1 - j, i)          -- rotate again
 * - Iterate j from i to n - i - 2 to avoid double-swapping corners.
 */
function rotate(matrix: number[][]): void {
  const n = matrix.length;
  const layers = Math.floor(n / 2);

  // Process each layer
  for (let i = 0; i < layers; i++) {
    // Process each element (except for the last one, else: double swapping)
    for (let j = i; j < n - i - 1; j++) {
      let temp = matrix[i][j]; // top
      matrix[i][j] = matrix[n - 1 - j][i]; // left -> top
      matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]; // bottom -> left
      matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]; // right -> bottom
      matrix[j][n - 1 - i] = temp; // top -> right
    }
  }
}
