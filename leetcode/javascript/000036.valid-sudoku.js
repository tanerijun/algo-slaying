/**
 * @param {character[][]} board
 * @return {boolean}
 * Time complexity: O(n^2)
 * Space complexity: O(n^2)
 */
var isValidSudoku = function (board) {
  const rows = new SetMap();
  const cols = new SetMap();
  const blocks = new SetMap(); // key = `${row // 3},${col // 3}`

  for (let r = 0; r < board.length; r++) {
    for (let c = 0; c < board[0].length; c++) {
      const n = board[r][c];

      if (n === ".") continue;

      if (
        rows.get(r).has(n) || cols.get(c).has(n) ||
        blocks.get(`${Math.floor(r / 3)},${Math.floor(c / 3)}`).has(n)
      ) {
        return false;
      }

      rows.get(r).add(n);
      cols.get(c).add(n);
      blocks.get(`${Math.floor(r / 3)},${Math.floor(c / 3)}`).add(n);
    }
  }

  return true;
};

class SetMap {
  constructor() {
    this.map = new Map();
  }

  get(key) {
    if (!this.map.has(key)) {
      this.map.set(key, new Set());
    }
    return this.map.get(key);
  }

  set(key, value) {
    this.map.set(key, value);
  }
}
