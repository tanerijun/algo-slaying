/**
 * @param {number[]} nums
 * @return {number[]}
 * Time complexity: O(n(log(n)))
 * Space complexity: O(n)
 */
var frequencySort = function (nums) {
  const countMap = new Map();
  for (const n of nums) {
    countMap.set(n, (countMap.get(n) ?? 0) + 1);
  }

  nums.sort((a, b) => {
    const countA = countMap.get(a);
    const countB = countMap.get(b);
    if (countA === countB) return b - a; // decreasing
    return countA - countB; // increasing
  });

  return nums;
};
