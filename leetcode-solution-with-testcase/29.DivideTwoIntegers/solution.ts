// Using subtraction
export function divide(dividend: number, divisor: number): number {
  if (dividend === 0) {
    return 0;
  }

  if (dividend === divisor) {
    return 1;
  }

  let res = 0;
  let isPositive = divisor < 0 === dividend < 0;

  if (divisor === 1 || divisor === -1) {
    res = Math.abs(dividend);
  }

  // Make both numbers positive
  dividend = Math.abs(dividend);
  divisor = Math.abs(divisor);

  if (res === 0) {
    let counter = 0; // track the number of substraction
    while (dividend >= 0) {
      dividend -= divisor;
      counter++;
    }

    // The last substraction doesn't count, so:
    res = --counter;
  }

  res = isPositive ? res : res * -1;

  // Handle overflow
  const MIN_INT = Math.pow(-2, 31);
  const MAX_INT = Math.pow(2, 31) - 1;

  if (res < MIN_INT) {
    return MIN_INT;
  } else if (res > MAX_INT) {
    return MAX_INT;
  }

  return res;
}
