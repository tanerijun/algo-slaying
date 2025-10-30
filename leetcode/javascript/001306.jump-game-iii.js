/**
 * @param {number[]} arr
 * @param {number} start
 * @return {boolean}
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
var canReach = function (arr, start) {
  const visited = new Set();

  function dfs(i) {
    if (i < 0 || i >= arr.length || visited.has(i)) return false;
    if (arr[i] === 0) return true;
    visited.add(i);
    return dfs(i - arr[i]) || dfs(i + arr[i]);
  }

  return dfs(start);
};
