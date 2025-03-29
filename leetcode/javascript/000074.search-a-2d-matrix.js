/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 * Time complexity: O(log(m * n))
 * Space complexity: O(1)
 */
var searchMatrix = function (matrix, target) {
  const ROW = matrix.length;
  const COL = matrix[0].length;

  let left = 0;
  let right = ROW * COL - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    const midRow = Math.floor(mid / COL);
    const midCol = mid - (midRow * COL);

    if (matrix[midRow][midCol] < target) {
      left = mid + 1;
    } else if (matrix[midRow][midCol] > target) {
      right = mid - 1;
    } else {
      return true;
    }
  }

  return false;
};
