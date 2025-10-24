/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 * Time complexity: O(n)
 * Space complexity: O(1)
 */
var myPow = function (x, n) {
  if (x === 1) return 1;
  if (x === -1) return n % 2 === 0 ? 1 : -1;
  let res = 1;
  isNegativeExp = n < 0;
  n = Math.abs(n);
  for (let i = 0; i < n; i++) {
    res *= x;
  }
  if (isNegativeExp) return 1 / res;
  return res;
};

/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 * Time complexity: O(log2(n))
 * Space complexity: O(log2(n))
 */
var myPow = function (x, n) {
  function helper(x, n) {
    if (n === 0) return 1;
    const temp = helper(x, Math.floor(n / 2));
    return n % 2 === 0 ? temp * temp : temp * temp * x;
  }
  return n < 0 ? 1 / helper(x, Math.abs(n)) : helper(x, Math.abs(n));
};
