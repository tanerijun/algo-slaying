// Time complexity: O(log(x)) - For a number x, the number of digits is approximately log₁₀(x)
// Space complexity: O(1)
function reverse(x: number): number {
  let input = Math.abs(x);
  let result = 0;

  while (input !== 0) {
    result = result * 10 + (input % 10);
    input = Math.floor(input / 10);
  }

  result *= Math.sign(x);

  if (result < Math.pow(-2, 31) || result > Math.pow(2, 31) - 1) return 0;

  return result;
}
