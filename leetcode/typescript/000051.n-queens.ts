// Time complexity: O(n!)
// Space complexity: O(n^2)
function solveNQueens(n: number): string[][] {
  const columnSet = new Set();
  const positiveDiagonalSet = new Set();
  const negativeDiagonalSet = new Set();
  const res: string[][] = [];
  const board: string[][] = Array(n).fill(null).map(() => Array(n).fill("."));

  function backtrack(r: number) {
    if (r === n) {
      res.push(board.map((row) => row.join("")));
      return;
    }

    for (let c = 0; c < n; c++) {
      if (
        columnSet.has(c) || positiveDiagonalSet.has(r + c) ||
        negativeDiagonalSet.has(r - c)
      ) {
        continue;
      }

      columnSet.add(c);
      positiveDiagonalSet.add(r + c);
      negativeDiagonalSet.add(r - c);
      board[r][c] = "Q";

      backtrack(r + 1);

      columnSet.delete(c);
      positiveDiagonalSet.delete(r + c);
      negativeDiagonalSet.delete(r - c);
      board[r][c] = ".";
    }
  }

  backtrack(0);
  return res;
}
