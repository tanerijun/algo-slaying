export function twoSum(numbers: number[], target: number): number[] {
  const res: number[] = [];

  let l = 0;
  let r = numbers.length - 1;

  while (l < r) {
    const sum = numbers[l] + numbers[r];

    if (sum < target || (l > 0 && numbers[l] === numbers[l - 1])) {
      l++;
    } else if (
      sum > target || (r < numbers.length - 1 && numbers[r] === numbers[r + 1])
    ) {
      r--;
    } else {
      res.push(l + 1, r + 1);
      l++;
      r--;
    }
  }

  return res;
}
