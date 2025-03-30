/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 * Time complexity: O(log(max(p)) * p) -> max(p) = maximum val in array p
 * Space complexity: O(1)
 */
var minEatingSpeed = function (piles, h) {
  let left = 1;
  let right = Math.max(...piles);
  let res = right;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    const curH = piles.reduce(
      (totalHours, bananas) => totalHours + Math.ceil(bananas / mid),
      0,
    );

    if (curH <= h) {
      right = mid - 1;
      res = Math.min(res, mid);
    } else {
      left = mid + 1;
    }
  }

  return res;
};
