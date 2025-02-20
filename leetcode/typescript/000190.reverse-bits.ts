// Time complexity: O(1)
// Space complexity: O(1)
function reverseBits(n: number): number {
  let res = 0;

  for (let i = 0; i < 32; i++) {
    const bit = (n >> i) & 1;
    res = res | (bit << (31 - i));
  }

  return res >>> 0; // convert to unsigned 32-bit integer
}
