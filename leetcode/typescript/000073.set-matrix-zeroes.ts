/**
 Do not return anything, modify matrix in-place instead.
 Time complexity: O(m * n)
 Space complexity: O(1)
 */
function setZeroes(matrix: number[][]): void {
  const rows = matrix.length;
  const cols = matrix[0].length;

  // Since (0, 0) can mean the whole col/row is zero, we reserve it for col
  // and track for row using this flag
  let firstRowZero = false;

  // Determine which rows and columns need to be zeroed
  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      if (matrix[row][col] === 0) {
        matrix[0][col] = 0; // marker on first row for column

        // Place marker on first column of the row
        // if it is not the first row in which case
        // we mark using the flag we set up already
        if (row > 0) {
          matrix[row][0] = 0;
        } else {
          firstRowZero = true;
        }
      }
    }
  }

  // Convert all rows except the first
  // and all columns except the first
  // to zero if they are marked as zero
  // in the first column and the first row
  for (let row = 1; row < rows; row++) {
    for (let col = 1; col < cols; col++) {
      if (matrix[0][col] === 0 || matrix[row][0] === 0) {
        matrix[row][col] = 0;
      }
    }
  }

  // Handle the first column as
  // the previous loop skipped it
  if (matrix[0][0] === 0) {
    for (let row = 0; row < rows; row++) {
      matrix[row][0] = 0;
    }
  }

  // Handle the first column as
  // the previous loop skipped it
  if (firstRowZero) {
    for (let col = 0; col < cols; col++) {
      matrix[0][col] = 0;
    }
  }
};
