// Time complexity: O(n)
// Space complexity: O(1)
function singleNumber(nums: number[]): number {
  let res = 0;
  for (const n of nums) {
    res ^= n;
  }
  return res;
}
