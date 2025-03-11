/**
 Do not return anything, modify board in-place instead.
 */
// Time complexity: O(m * n)
// Space complexity: O(m * n)
function solve(board: string[][]): void {
  const rows = board.length;
  const cols = board[0].length;

  function dfs(r: number, c: number): void {
    if (r < 0 || c < 0 || r >= rows || c >= cols || board[r][c] !== "O") {
      return;
    }
    board[r][c] = "."; // mark as unsurrounded
    dfs(r - 1, c);
    dfs(r + 1, c);
    dfs(r, c - 1);
    dfs(r, c + 1);
  }

  for (let c = 0; c < cols; c++) {
    dfs(0, c);
    dfs(rows - 1, c);
  }

  for (let r = 0; r < rows; r++) {
    dfs(r, 0);
    dfs(r, cols - 1);
  }

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (board[r][c] === "O") board[r][c] = "X";
      if (board[r][c] === ".") board[r][c] = "O"; // remove mark
    }
  }
}
