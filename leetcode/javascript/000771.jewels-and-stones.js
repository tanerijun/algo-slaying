/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 * Time complexity: O(n) - n = length of stones
 * Space complexity: O(1)
 * Length of jewels can be considered constant for there can only be 52 jewels at most (a-zA-Z)
 */
var numJewelsInStones = function(jewels, stones) {
  let count = 0;
  for (const stone of stones) {
    if (jewels.includes(stone)) count++;
  }
  return count;
};
