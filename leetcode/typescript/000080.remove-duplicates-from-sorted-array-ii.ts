function removeDuplicates(nums: number[]): number {
  const currentNumber = {
    value: nums[0],
    count: 1,
  };

  let idx = 1;

  for (let i = 1; i < nums.length; i++) {
    if (nums[i] === currentNumber.value && currentNumber.count === 2) {
      continue;
    }

    if (nums[i] === currentNumber.value && currentNumber.count < 2) {
      currentNumber.count++;
    }

    if (nums[i] !== currentNumber.value) {
      currentNumber.count = 1;
      currentNumber.value = nums[i];
    }

    const temp = nums[idx];
    nums[idx] = nums[i];
    nums[i] = temp;

    idx++;
  }

  return idx;
}
// Time complexity: O(n)
// Space complexity: O(1)
