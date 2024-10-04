function shipWithinDays(weights: number[], days: number): number {
  // 1. The minimum ship capacity is the maximum weight
  // 2. The maximum ship capacity is the total of all weights
  // 3. We can solve this efficiently, by running binary search on the resulting ranges

  let max = 0;
  let total = 0;
  for (const weight of weights) {
    max = Math.max(max, weight);
    total += weight;
  }

  // Binary search
  let l = max;
  let r = total;
  let res = r;

  while (l <= r) {
    const m = Math.floor((l + r) / 2);

    let nDays = 1;
    let sum = 0;
    for (const weight of weights) {
      if (sum + weight > m) {
        nDays++;
        sum = 0;
      }

      sum += weight;
    }

    if (nDays <= days) {
      res = Math.min(res, m);
      r = m - 1;
    } else {
      l = m + 1;
    }
  }

  return res;
}
// Time complexity: O(n * log n)
// Space complexity: O(1)
