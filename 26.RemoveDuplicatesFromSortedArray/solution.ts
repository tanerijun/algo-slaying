// Return value slightly modified in order to test the array.
export function removeDuplicates(nums: number[]): [number, number[]] {
  let idx = 1;

  for (let i = 1; i < nums.length; i++) {
    if (nums[i - 1] !== nums[i]) {
      nums[idx++] = nums[i];
    }
  }

  return [idx, nums];
};