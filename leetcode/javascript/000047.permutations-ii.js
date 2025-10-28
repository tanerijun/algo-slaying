/**
 * @param {number[]} nums
 * @return {number[][]}
 * Time complexity: O(n * n!)
 * Space complexity: O(n)
 */
var permuteUnique = function (nums) {
  nums.sort((a, b) => a - b);
  const res = [];
  const temp = [];
  const used = new Set();

  function backtrack() {
    if (temp.length === nums.length) {
      res.push([...temp]);
      return;
    }

    for (let i = 0; i < nums.length; i++) {
      if (used.has(i)) continue;
      if (i > 0 && nums[i] === nums[i - 1] && !used.has(i - 1)) continue;
      used.add(i);
      temp.push(nums[i]);
      backtrack();
      temp.pop();
      used.delete(i);
    }
  }

  backtrack();
  return res;
};
