/**
 Do not return anything, modify nums in-place instead.
 */
function rotate(nums: number[], k: number): void {
  function reverse(l: number, r: number) {
    while (l < r) {
      const temp = nums[l];
      nums[l] = nums[r];
      nums[r] = temp;

      l++;
      r--;
    }
  }

  k = k % nums.length;

  // Reverse the whole array
  reverse(0, nums.length - 1);

  // Reverse the first k nums
  reverse(0, k - 1);

  // Reverse the rest
  reverse(k, nums.length - 1);
}
// Time complexity: O(n)
// Space complexity: O(1)

/**
 * Explanation:
 * k = 3
 * 1234567
 * 765 4321
 * 567 1234
 *
 * Alternative:
 * Another approach using O(n) space is to loop through each num, add each with k % len(nums),
 * and copy the array back to the original array
 */
