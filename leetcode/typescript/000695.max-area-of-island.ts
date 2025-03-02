// Time complexity: O(m * n)
// Space complexity: O(m * n)
function maxAreaOfIsland(grid: number[][]): number {
  const rows = grid.length;
  const cols = grid[0].length;
  const visited = new Set<string>();
  let maxArea = 0;

  function bfs(r: number, c: number) {
    const queue = [[r, c]];
    let area = 0;

    while (queue.length > 0) {
      const [r, c] = queue.shift()!;
      visited.add(`${r},${c}`);
      area++;

      const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      for (const [dr, dc] of directions) {
        const newR = r + dr;
        const newC = c + dc;

        if (
          newR < 0 || newC < 0 || newR >= rows || newC >= cols ||
          grid[newR][newC] === 0 ||
          visited.has(`${newR},${newC}`)
        ) {
          continue;
        }

        queue.push([newR, newC]);
        visited.add(`${newR},${newC}`);
      }
    }

    maxArea = Math.max(maxArea, area);
  }

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (grid[r][c] !== 0 && !visited.has(`${r},${c}`)) {
        bfs(r, c);
      }
    }
  }

  return maxArea;
}
