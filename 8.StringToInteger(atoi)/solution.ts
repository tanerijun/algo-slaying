export function myAtoi(s: string): number {
  const input: string = s.trimStart();
  let result: number = 0;
  let sign: number | undefined;

  if (input[0] === '+') {
    sign = 1;
  } else if (input[0] === '-') {
    sign = -1;
  }

  let i = sign ? 1 : 0;
  for (; i < input.length; i++) {
    const num = parseInt(input[i]);
    if (num >= 0 && num <= 9) {
      result = result * 10 + num;
    } else {
      break;
    }
  }

  result = sign === -1 ? result * -1 : result;

  const MAX_VAL = Math.pow(2, 31) - 1;
  const MIN_VAL = Math.pow(-2, 31);

  if (result > MAX_VAL) {
    result = MAX_VAL;
  } else if (result < MIN_VAL) {
    result = MIN_VAL;
  }

  return result;
};