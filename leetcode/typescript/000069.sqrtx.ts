function mySqrt(x: number): number {
  if (x === 0) return 0;
  let l = 1;
  let r = x;
  while (l < r) {
    const m = Math.ceil((l + r) / 2);
    const mSquared = m * m;
    if (mSquared > x) {
      r = m - 1;
    } else if (mSquared < x) {
      l = m + 1;
    } else {
      return m;
    }
  }

  const lSquared = l * l;
  return lSquared === x ? l : lSquared > x ? l - 1 : l;
}
// Time complexity: O(Log n)
// Space complexity: O(1)
