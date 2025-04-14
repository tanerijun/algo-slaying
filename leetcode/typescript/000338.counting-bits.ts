// Time complexity: O(nlog(n)) -> log(n) because in general a number i needs [log₂(i)] + 1 bits
// Space complexity: O(1)
function countBits(n: number): number[] {
  const res: number[] = [];

  for (let i = 0; i <= n; i++) {
    let num = i;
    let temp = 0;
    while (num > 0) {
      temp += num & 1;
      num >>= 1;
    }
    res.push(temp);
  }

  return res;
}

// Time complexity: O(n)
// Space complexity: O(1) -> depends on if we count dp array as extra space or not (it's also the ans array)
function countBit2(n: number): number[] {
  const dp = Array(n + 1).fill(0);
  let offset = 1; // largest most-significant-bit reached

  for (let i = 1; i <= n; i++) {
    if (offset * 2 === i) offset = i;
    dp[i] = 1 + dp[i - offset];
  }

  return dp;
}
