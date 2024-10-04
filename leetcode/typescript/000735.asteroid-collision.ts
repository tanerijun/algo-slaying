function asteroidCollision(asteroids: number[]): number[] {
  const stack: number[] = [];

  for (let asteroid of asteroids) {
    while (stack && stack[stack.length - 1] > 0 && asteroid < 0) {
      const sizeAfterCollision = stack[stack.length - 1] + asteroid;

      if (sizeAfterCollision < 0) {
        stack.pop();
      } else if (sizeAfterCollision > 0) {
        asteroid = 0;
      } else {
        stack.pop();
        asteroid = 0;
      }
    }

    if (asteroid) {
      stack.push(asteroid);
    }
  }

  return stack;
}
// Time complexity: O(n)
// Space complexity: O(n)
