// Time complexity: O(n(log(n)))
// Space complexity: O(1)
function missingNumber(nums: number[]): number {
  const n = nums.length;
  nums.sort((a, b) => a - b);
  for (let i = 0; i < n; i++) {
    if (nums[i] !== i) {
      return i;
    }
  }
  return n;
}

// Time complexity: O(n)
// Space complexity: O(n)
function missingNumber2(nums: number[]): number {
  const numSet = new Set(nums);
  const n = nums.length;
  for (let i = 0; i <= n; i++) {
    if (!numSet.has(i)) {
      return i;
    }
  }
}

// Time complexity: O(n)
// Space complexity: O(1)
function missingNumber3(nums: number[]): number {
  const n = nums.length;
  let res = n;
  for (let i = 0; i < n; i++) {
    res = res ^ i ^ nums[i];
  }
  return res;
}

// Time complexity: O(n)
// Space complexity: O(1)
function missingNumber4(nums: number[]): number {
  const n = nums.length;
  let res = n;
  for (let i = 0; i < n; i++) {
    res += i - nums[i];
  }
  return res;
}

// Time complexity: O(n)
// Space complexity: O(1)
function missingNumber5(nums: number[]): number {
  const n = nums.length;
  const expectedSum = (n * (n + 1)) / 2;
  const actualSum = nums.reduce((sum, num) => sum + num, 0);
  return expectedSum - actualSum;
}
