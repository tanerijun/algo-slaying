/**
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	     -1 if num is higher than the picked number
 * 			      1 if num is lower than the picked number
 *               otherwise return 0
 * var guess = function(num) {}
 */

var guess = function (num: number) {
  return num;
}; // dummy implementation for TS

function guessNumber(n: number): number {
  let l = 1;
  let r = n;

  while (true) {
    let m = Math.floor((l + r) / 2);
    if (guess(m) === -1) {
      r = m - 1;
    } else if (guess(m) === 1) {
      l = m + 1;
    } else {
      return m;
    }
  }
}
// Time complexity: O(n)
// Space complexity: O(n)
