/* Using String
export function reverse(x: number): number {
  const reversed = x.toString().split("").reverse().join("");
  const result = parseInt(reversed) * Math.sign(x);

  if (result < Math.pow(-2, 31) || result > Math.pow(2, 31) - 1) return 0;

  return result;
}; */

// Using arithmetic
export function reverse(x: number): number {
  let input = Math.abs(x);
  let result: number = 0;

  while (input != 0) {
    result = result * 10 + input % 10;
    input = Math.floor(input / 10);
  }

  result *= Math.sign(x);

  if (result < Math.pow(-2, 31) || result > Math.pow(2, 31) - 1) return 0;

  return result;
};