function validateStackSequences(pushed: number[], popped: number[]): boolean {
  const stack: number[] = [];

  let toPopIdx = 0;
  for (const toPush of pushed) {
    stack.push(toPush);

    while (
      stack && toPopIdx < popped.length &&
      stack[stack.length - 1] === popped[toPopIdx]
    ) {
      stack.pop();
      toPopIdx++;
    }
  }

  return stack.length === 0;
}
