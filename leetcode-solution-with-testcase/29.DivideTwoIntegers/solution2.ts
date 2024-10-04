// Using bitwise left shift (<<)
export function divide(dividend: number, divisor: number): number {
  if (dividend === 0) {
    return 0;
  }

  if (dividend === divisor) {
    return 1;
  }

  let res = 0;
  let isPositive = divisor < 0 === dividend < 0;
  dividend = Math.abs(dividend);
  divisor = Math.abs(divisor);

  if (res === 0) {
    while (dividend >= divisor) {
      let n = 0;

      // JS converts number to signed 32-bit int automatically when we do bitwise operation
      // So, we need to handle the edge case where the number will overflow
      // e.g: divide(-2147483648, -1)
      // The 30th << will cause the n to turn negative and we'll get stuck in an infinite loop
      // So let's simulate << using Math.pow instead
      // After all, a << n = a * 2^n
      while (dividend > divisor * Math.pow(2, n + 1)) {
        n++;
      }

      res += Math.pow(2, n);
      dividend -= divisor * Math.pow(2, n);
    }
  }

  res = handleNegative(res, isPositive);
  res = handleOverflow(res);

  return res;
}

function handleNegative(n: number, isPositive: boolean) {
  return isPositive ? n : n * -1;
}

function handleOverflow(n: number) {
  const MIN_INT = Math.pow(-2, 31);
  const MAX_INT = Math.pow(2, 31) - 1;

  if (n < MIN_INT) {
    return MIN_INT;
  } else if (n > MAX_INT) {
    return MAX_INT;
  } else {
    return n;
  }
}
