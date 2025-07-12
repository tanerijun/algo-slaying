/**
 * @param {number[]} nums
 * @return {number}
 * Time complexity: O(2 ^ n)
 * Space complexity: O(n)
 */
var subsetXORSum = function (nums) {
  function dfs(i, current_xor) {
    if (i === nums.length) {
      return current_xor;
    }

    return dfs(i + 1, current_xor ^ nums[i]) + dfs(i + 1, current_xor);
  }

  return dfs(0, 0);
};
