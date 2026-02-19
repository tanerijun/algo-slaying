/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 * Time complexity: O(log(n))
 * Space complexity: O(1)
 */
var findKthPositive = function (arr, k) {
  let l = 0;
  let r = arr.length - 1;

  while (l <= r) {
    const m = Math.floor((l + r) / 2);
    const missingCount = arr[m] - 1 - m;

    if (missingCount < k) {
      l = m + 1;
    } else {
      r = m - 1;
    }
  }

  // r = -1 means k missing numbers all come before arr[0]
  if (r < 0) return k;

  const missingCount = arr[r] - 1 - r;
  return arr[r] + (k - missingCount);
};
