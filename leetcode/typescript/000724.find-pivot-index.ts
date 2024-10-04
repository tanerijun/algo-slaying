function pivotIndex(nums: number[]): number {
  let res = -1;
  const map = new Map<number, number>();

  for (let i = 0; i < nums.length; i++) {
    const previousSum = map.get(i - 1) ?? 0;
    map.set(i, nums[i] + previousSum);
  }

  for (let i = 0; i < nums.length; i++) {
    const leftSum = map.get(i - 1) ?? 0;
    const totalSum = map.get(nums.length - 1) as number;
    const sumUpToIdx = map.get(i) as number;
    const rightSum = totalSum - sumUpToIdx;

    if (leftSum === rightSum) {
      res = i;
      break;
    }
  }

  return res;
}
// Time complexity: O(n)
// Space complexity: O(n)
