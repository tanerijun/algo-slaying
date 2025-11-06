/**
 * @param {number[]} arr
 * @return {number}
 * Time complexity: O(n)
 * Space complexity: O(1)
 * Intuition:
 * - We only need to know check how long the pattern is going
 * - We only care about the previous direction (1 state)
 * - Did the pattern alternate? Increment counter
 * - Did the pattern break? Reset counter
 */
var maxTurbulenceSize = function (arr) {
  let res = 0;
  let count = 0;
  let sign = -1; // -1 reset, 1 previous was >, -1, previous was <

  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] > arr[i + 1]) {
      count = sign === 0 ? count + 1 : 1;
      sign = 1;
    } else if (arr[i] < arr[i + 1]) {
      count = sign === 1 ? count + 1 : 1;
      sign = 0;
    } else {
      count = 0;
      sign = -1;
    }

    res = Math.max(res, count);
  }

  // +1 because we only counts the valid comparisons
  // The number of elements is n_comparisons + 1
  // Ex: 1 < 2, n_comparisons = 1, n_elements = 2
  return res + 1;
};
