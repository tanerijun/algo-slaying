export function threeSumClosest(nums: number[], target: number): number {

  nums.sort((a, b) => a - b);
  let result = nums[0] + nums[1] + nums[2];
  let l = 0;
  let r = 0;

  for (let i = 0; i < nums.length - 2; i++) {
    l = i + 1;
    r = nums.length - 1;

    while (l < r) {
      const sum = nums[i] + nums[l] + nums[r]

      if (sum < target) {
        l++;
      } else if (sum > target) {
        r--;
      } else {
        return sum;
      }

      if (Math.abs(target - sum) < Math.abs(target - result)) {
        result = sum;
      }
    }
  }

  return result;
};