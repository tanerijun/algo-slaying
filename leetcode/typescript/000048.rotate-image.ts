/**
 Time complexity: O(n2)
 Space complexity: O(1)
 */
function rotate(matrix: number[][]): void {
  const n = matrix.length;
  const layers = Math.floor(n / 2);

  // Process each layer
  for (let i = 0; i < layers; i++) {
    // Process each element (except for the last one, else: double swapping)
    for (let j = i; j < n - i - 1; j++) {
      let temp = matrix[i][j]; // save TL
      matrix[i][j] = matrix[n - 1 - j][i]; // BL → TL
      matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]; // BR → BL
      matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]; // TR → BR
      matrix[j][n - 1 - i] = temp; // TL -> TR
    }
   }
};
