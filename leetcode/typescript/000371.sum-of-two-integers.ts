// Time complexity: O(1)
// Space complexity: O(1)
function getSum(a: number, b: number): number {
  while (b != 0) {
    const temp = (a & b) << 1;
    a = a ^ b;
    b = temp;
  }
  return a;
}
