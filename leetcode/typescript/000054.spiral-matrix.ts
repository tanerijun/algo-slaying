// Time complexity: O(n * m)
// Space complexity: O(1)
function spiralOrder(matrix: number[][]): number[] {
  const res: number[] = [];
  let rowBegin = 0;
  let colBegin = 0;
  let rowEnd = matrix.length - 1;
  let colEnd = matrix[0].length - 1;

  while (rowBegin <= rowEnd && colBegin <= colEnd) {
    // traverse right
    for (let i = colBegin; i <= colEnd; i++) {
      res.push(matrix[rowBegin][i]);
    }
    rowBegin++;

    // traverse down
    for (let i = rowBegin; i <= rowEnd; i++) {
      res.push(matrix[i][colEnd]);
    }
    colEnd--;

    if (rowBegin <= rowEnd) {
      // traverse left
      for (let i = colEnd; i >= colBegin; i--) {
        res.push(matrix[rowEnd][i]);
      }
      rowEnd--;
    }

    if (colBegin <= colEnd) {
      // traverse up
      for (let i = rowEnd; i >= rowBegin; i--) {
        res.push(matrix[i][colBegin]);
      }
      colBegin++;
    }
  }

  return res;
};
