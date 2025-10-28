/**
 * @param {number[]} nums
 * @return {number[][]}
 * Time complexity: O(n.n!) - permutation count and work per permutation (array copy, and array.includes check)
 * Space complexity: O(n) - stack space
 */
var permute = function (nums) {
  const res = [];
  const temp = [];

  function backtrack() {
    if (temp.length === nums.length) {
      res.push([...temp]);
      return;
    }

    for (const num of nums) {
      if (temp.includes(num)) continue;
      temp.push(num);
      backtrack();
      temp.pop();
    }
  }

  backtrack();
  return res;
};
