// Time complexity: O(1) -> n is guaranteed to be a 32-bit number
// Space complexity: O(1)
function hammingWeight(n: number): number {
  let res = 0;

  while (n > 0) {
    res += n % 2;
    n = n >> 1;
  }

  return res;
}

// Time complexity: O(1) -> n is guaranteed to be a 32-bit number
// Space complexity: O(1)
function hammingWeight2(n: number): number {
  let res = 0;

  while (n > 0) {
    res += n & 1;
    n = n >> 1;
  }

  return res;
}

// Even more efficient
// Time complexity: O(1) -> less than 32x as it only run for each `1` in the bits
// Space complexity: O(1)
function hammingWeight3(n: number): number {
  let res = 0;

  while (n > 0) {
    res += 1;
    n = n & (n - 1);
  }

  return res;
}
