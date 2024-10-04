function removeElement(nums: number[], val: number): number {
  let i = 0;
  let j = nums.length - 1;

  while (i <= j) {
    if (nums[i] === val) {
      const temp = nums[i];
      nums[i] = nums[j];
      nums[j] = temp;
      j--;
    } else {
      i++;
    }
  }

  return i;
}
// Time complexity: O(n)
// Space compolexity: O(1)
