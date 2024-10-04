function numberOfSteps(num: number): number {
  let steps = 0;

  while (num !== 0) {
    if (num % 2 !== 0) {
      num--;
    } else {
      num /= 2;
    }

    steps++;
  }

  return steps;
}
// Time complexity: O(log n) - The time complexity from executing `num--` is irrelevant relative to `num /= 2`
// Space complexity: O(1)
