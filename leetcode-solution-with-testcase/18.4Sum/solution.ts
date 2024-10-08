export function fourSum(nums: number[], target: number): number[][] {
  nums.sort((a, b) => a - b);

  return kSum(nums, target, 4);
}

// twoSum solution using two pointers
// nums should be sorted beforehand
export function twoSum(nums: number[], target: number): number[][] {
  const res: number[][] = [];

  let l = 0;
  let r = nums.length - 1;

  while (l < r) {
    const sum = nums[l] + nums[r];

    if (sum < target || (l > 0 && nums[l] === nums[l - 1])) {
      l++;
    } else if (
      sum > target || (r < nums.length - 1 && nums[r] === nums[r + 1])
    ) {
      r--;
    } else {
      res.push([nums[l], nums[r]]);
      l++;
      r--;
    }
  }

  return res;
}

// kSum using two pointers
// With kSum, we can also solve 5Sum, 6Sum, ...
// Time Complexity: O(n^(k - 1)), k-2 loops and twoSum is O(n)
// With kSum, we want to recurse and reduce the size of the problem until all that's left is twoSum.
// Nums should be sorted beforehand
function kSum(nums: number[], target: number, k: number): number[][] {
  const res: number[][] = [];

  if (!nums) {
    return res;
  }

  const avgVal = Math.trunc(target / k);

  if (avgVal < nums[0] || nums[nums.length - 1] < avgVal) {
    return res;
  }

  if (k === 2) {
    return twoSum(nums, target);
  }

  for (let i = 0; i < nums.length; i++) {
    if (i === 0 || nums[i - 1] != nums[i]) {
      // If in this example our nums[i] = -2, then the sum of the remaining array have to be 2.
      // Hence kSum(nums.slice(1+1), target - nums[i], k - 1)
      for (const subset of kSum(nums.slice(i + 1), target - nums[i], k - 1)) {
        res.push([nums[i]].concat(subset));
      }
    }
  }

  return res;
}
