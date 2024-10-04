/**
 Do not return anything, modify nums in-place instead.
 */
function sortColors(nums: number[]): void {
  let l = 0;
  let m = 0;
  let r = nums.length - 1;
  let temp: number;

  while (m <= r) {
    switch (nums[m]) {
      case 0:
        temp = nums[l];
        nums[l] = nums[m];
        nums[m] = temp;
        l++;
        m++;
        break;
      case 1:
        m++;
        break;
      case 2:
        temp = nums[r];
        nums[r] = nums[m];
        nums[m] = temp;
        r--;
        break;
      default:
        throw new Error("possible values should be 0, 1, 2");
    }
  }
}
// Time complexity: O(n)
// Space complecity: O(1)
