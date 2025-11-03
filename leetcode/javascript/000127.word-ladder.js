/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 * Time complexity: O(n * m) - For every node, for every char in node, try replacing with other chars (a-z (26))
 * Space complexity: O(n) - Storing all n words in set
 *
 * - Each word is a node in a graph
 * - 2 words are connected if they differ by 1 letter
 * - To find shortest path in graph, use BFS
 * - BFS always explores the shortest path first
 */
var ladderLength = function (beginWord, endWord, wordList) {
  const queue = [];
  queue.push([beginWord, 1]);

  // Set serve 2 purposes here: Dictionary lookup & Visited tracking
  const set = new Set(wordList);
  if (!set.has(endWord)) return 0;

  while (queue.length) {
    const [word, steps] = queue.shift();

    if (word === endWord) return steps;

    for (let i = 0; i < word.length; i++) {
      for (let ch = 97; ch <= 122; ch++) { // a-z
        const newChar = String.fromCharCode(ch);
        if (newChar === word[i]) continue; // skip self

        const newWord = word.slice(0, i) + newChar + word.slice(i + 1);

        if (set.has(newWord)) {
          // Why delete from set: Prevents infinite loops and ensures we don't explore the same word multiple times.
          // Once we've found a word at step N, any future path to that word will be ≥ N steps.
          set.delete(newWord);
          queue.push([newWord, steps + 1]);
        }
      }
    }
  }

  return 0;
};
