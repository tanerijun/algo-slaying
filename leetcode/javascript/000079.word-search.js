/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 * Time complexity: O(m * n * 4^L) -> 4 choices per step
 * Space complexity: O(L)
 */
var exist = function (board, word) {
  function key(r, c) {
    return `${r},${c}`;
  }

  const rows = board.length;
  const cols = board[0].length;
  const visited = new Set();

  function dfs(i, r, c) {
    if (
      r < 0 || c < 0 || r >= rows || c >= cols || visited.has(key(r, c)) ||
      board[r][c] !== word[i]
    ) {
      return false;
    }

    if (i === word.length - 1) {
      return true;
    }

    visited.add(key(r, c));
    const result = dfs(i + 1, r - 1, c) || dfs(i + 1, r + 1, c) ||
      dfs(i + 1, r, c - 1) || dfs(i + 1, r, c + 1);
    visited.delete(key(r, c));

    return result;
  }

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (dfs(0, r, c)) {
        return true;
      }
    }
  }

  return false;
};
