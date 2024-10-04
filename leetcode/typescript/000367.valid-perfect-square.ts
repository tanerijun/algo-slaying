function isPerfectSquare(num: number): boolean {
  let l = 0;
  let r = num;
  while (l <= r) {
    const m = Math.floor((l + r) / 2);
    const mSquared = m * m;
    if (mSquared === num) {
      return true;
    } else if (mSquared > num) {
      r = m - 1;
    } else {
      l = m + 1;
    }
  }
  return false;
}
// Time complexity: O(n)
// Space complexity: O(1)
