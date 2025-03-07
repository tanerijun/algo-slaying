// Time complexity: O(m * n)
// Space complexity: O(m * n)
function orangesRotting(grid: number[][]): number {
  const rows = grid.length;
  const cols = grid[0].length;
  let queue = [];
  let clock = 0;
  let freshOranges = 0;

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (grid[r][c] === 0) {
        continue;
      }
      if (grid[r][c] === 1) {
        freshOranges++;
      }
      if (grid[r][c] === 2) {
        queue.push([r, c]);
      }
    }
  }

  while (queue.length > 0) {
    const temp: [number, number][] = [];
    for (const [r, c] of queue) {
      for (const [dr, dc] of [[-1, 0], [1, 0], [0, -1], [0, 1]]) {
        const newR = r + dr;
        const newC = c + dc;
        if (
          newR >= 0 && newC >= 0 && newR < rows && newC < cols &&
          grid[newR][newC] === 1
        ) {
          freshOranges--;
          grid[newR][newC] = 2;
          temp.push([newR, newC]);
        }
      }
    }

    queue = temp;

    if (temp.length > 0) {
      clock++;
    }
  }

  return freshOranges > 0 ? -1 : clock;
}
