function searchMatrix(matrix: number[][], target: number): boolean {
  let rows = matrix.length;
  let cols = matrix[0].length;
  let total = rows * cols;

  let l = 0;
  let r = total - 1;

  while (l <= r) {
    let m = Math.floor((l + r) / 2);
    // To find out in which row the nth element is, m / number of elements in a row
    // To find out the in which column it is, use the remainder of the division above
    let mVal = matrix[Math.floor(m / cols)][m % cols];

    if (mVal > target) {
      r = m - 1;
    } else if (mVal < target) {
      l = m + 1;
    } else {
      return true;
    }
  }

  return false;
}
// Time complexity: O(log(n))
// Space complexity: O(1)
