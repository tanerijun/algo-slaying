// Time complexity: O(n)
// Space complexity: O(1)
function maxProduct(nums: number[]): number {
  let res = Math.max(...nums);
  let curMin = 1;
  let curMax = 1;

  for (const n of nums) {
    if (n === 0) {
      curMin = 1;
      curMax = 1;
      continue;
    }

    const tmp = curMax * n;
    curMax = Math.max(tmp, curMin * n, n);
    curMin = Math.min(tmp, curMin * n, n);
    res = Math.max(curMax, res);
  }

  return res;
}

// Time complexity: O(n)
// Space complexity: O(1)
function maxProduct2(nums: number[]): number {
  let res = nums[0];
  let leftProduct = 1;
  let rightProduct = 1;

  for (let i = 0; i < nums.length; i++) {
    leftProduct = leftProduct === 0 ? 1 : leftProduct;
    rightProduct = rightProduct === 0 ? 1 : rightProduct;

    leftProduct *= nums[i];
    rightProduct *= nums[nums.length - 1 - i];

    res = Math.max(leftProduct, rightProduct, res);
  }

  return res;
}
