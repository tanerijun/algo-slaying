// Time complexity: O(m * n)
// Space complexity: O(m * n)
function numIslands(grid: string[][]): number {
  if (!grid) return 0;

  const rows = grid.length;
  const cols = grid[0].length;
  const visited = new Set<string>();
  let islands = 0;

  function bfs(r: number, c: number) {
    const queue: Array<[number, number]> = [[r, c]];

    while (queue.length > 0) {
      const [r, c] = queue.shift()!;
      visited.add(`${r},${c}`);

      const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];
      for (const [dr, dc] of directions) {
        const newR = r + dr;
        const newC = c + dc;
        if (
          newR < 0 || newC < 0 || newR >= rows || newC >= cols ||
          grid[newR][newC] === "0" || visited.has(`${newR},${newC}`)
        ) {
          continue;
        }
        queue.push([newR, newC]);
        visited.add(`${newR},${newC}`);
      }
    }
  }

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (grid[r][c] === "0" || visited.has(`${r},${c}`)) continue;
      bfs(r, c);
      islands++;
    }
  }

  return islands;
}

function numIslands2(grid: string[][]): number {
  const rows = grid.length;
  const cols = grid[0].length;
  const visited = new Set<string>();
  let islands = 0;

  function dfs(r: number, c: number): void {
    if (
      r < 0 || c < 0 || r >= rows || c >= cols || visited.has(`${r},${c}`) ||
      grid[r][c] === "0"
    ) {
      return;
    }

    visited.add(`${r},${c}`);

    dfs(r - 1, c);
    dfs(r + 1, c);
    dfs(r, c - 1);
    dfs(r, c + 1);
  }

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (grid[r][c] === "1" && !visited.has(`${r},${c}`)) {
        dfs(r, c);
        islands++;
      }
    }
  }

  return islands;
}
