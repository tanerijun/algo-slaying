/**
 * @param {character[][]} board
 * @param {string[]} words
 * @return {string[]}
 * Time complexity: O(m * n * 4 * 3^(t - 1) + s)
 * Space complexity: O(s)
 * t = max word length in words
 * s = sum of word lengths in words
 */
var findWords = function (board, words) {
  const root = new TrieNode();
  for (const word of words) {
    root.addWord(word);
  }

  const rows = board.length;
  const cols = board[0].length;
  const visited = new Set();
  const res = [];

  function dfs(r, c, node, word) {
    if (
      r < 0 || c < 0 ||
      r >= rows || c >= cols ||
      visited.has(`${r},${c}`) ||
      !node.children.has(board[r][c])
    ) {
      return;
    }

    visited.add(`${r},${c}`);
    const nextNode = node.children.get(board[r][c]);
    const newWord = word + board[r][c];

    if (nextNode.isWord) {
      res.push(newWord);
      nextNode.isWord = false; // mark as found, prevent adding duplicates
    }

    dfs(r + 1, c, nextNode, newWord);
    dfs(r - 1, c, nextNode, newWord);
    dfs(r, c + 1, nextNode, newWord);
    dfs(r, c - 1, nextNode, newWord);

    visited.delete(`${r},${c}`);

    // Optimization: Delete leaf node
    if (nextNode.children.size === 0 && !nextNode.isWord) {
      node.children.delete(board[r][c]);
    }
  }

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      dfs(r, c, root, "");
    }
  }

  return res;
};

class TrieNode {
  constructor() {
    this.children = new Map();
    this.isWord = false;
  }

  addWord(word) {
    let cur = this;
    for (const ch of word) {
      if (!cur.children.has(ch)) {
        cur.children.set(ch, new TrieNode());
      }
      cur = cur.children.get(ch);
    }
    cur.isWord = true;
  }
}
