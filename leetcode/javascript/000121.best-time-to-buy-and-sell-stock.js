/**
 * @param {number[]} prices
 * @return {number}
 * Time complexity: O(n)
 * Space complexity: O(1)
 */
var maxProfit = function (prices) {
  let currMin = prices[0];
  let ans = 0;

  for (const price of prices) {
    currMin = Math.min(currMin, price);
    ans = Math.max(ans, price - currMin);
  }

  return ans;
};
