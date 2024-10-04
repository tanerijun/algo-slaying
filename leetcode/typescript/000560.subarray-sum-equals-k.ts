function subarraySum(nums: number[], k: number): number {
  let res = 0;
  let prefixSum = 0;
  let prefixSums = new Map<number, number>();
  prefixSums.set(0, 1);

  for (const num of nums) {
    prefixSum += num;
    res += prefixSums.get(prefixSum - k) ?? 0;
    prefixSums.set(prefixSum, (prefixSums.get(prefixSum) ?? 0) + 1);
  }

  return res;
}
// Time complexity: O(n)
// Space complexity: O(n)
