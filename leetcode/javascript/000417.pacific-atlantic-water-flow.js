/**
 * @param {number[][]} heights
 * @return {number[][]}
 * Time complexity: O(m * n)
 * Space complexity: O(m * n)
 */
var pacificAtlantic = function (heights) {
  const rows = heights.length;
  const cols = heights[0].length;
  const pQueue = new Queue();
  const aQueue = new Queue();
  const pSeen = new Set();
  const aSeen = new Set();

  function toSetKey(r, c) {
    return `${r},${c}`;
  }

  function fromSetKey(key) {
    return key.split(",").map(Number);
  }

  for (let c = 0; c < cols; c++) {
    pQueue.enqueue([0, c]);
    pSeen.add(toSetKey(0, c));
  }

  for (let r = 1; r < rows; r++) {
    pQueue.enqueue([r, 0]);
    pSeen.add(toSetKey(r, 0));
  }

  for (let c = 0; c < cols; c++) {
    aQueue.enqueue([rows - 1, c]);
    aSeen.add(toSetKey(rows - 1, c));
  }

  for (let r = 0; r < rows - 1; r++) {
    aQueue.enqueue([r, cols - 1]);
    aSeen.add(toSetKey(r, cols - 1));
  }

  function bfs(queue, seen) {
    while (!queue.isEmpty()) {
      const [r, c] = queue.dequeue();

      for (const [r_off, c_off] of [[-1, 0], [1, 0], [0, 1], [0, -1]]) {
        const newR = r + r_off;
        const newC = c + c_off;

        if (
          newR >= 0 && newC >= 0 && newR < rows && newC < cols &&
          !seen.has(toSetKey(newR, newC)) &&
          heights[newR][newC] >= heights[r][c]
        ) {
          queue.enqueue([newR, newC]);
          seen.add(toSetKey(newR, newC));
        }
      }
    }
  }

  bfs(pQueue, pSeen);
  bfs(aQueue, aSeen);

  return Array.from(pSeen.intersection(aSeen)).map((setKey) =>
    fromSetKey(setKey)
  );
};

// Cleaned up
var pacificAtlantic2 = function (heights) {
  const rows = heights.length;
  const cols = heights[0].length;
  const pSeen = new Set();
  const aSeen = new Set();
  const pQueue = new Queue();
  const aQueue = new Queue();

  function toSetKey(r, c) {
    return `${r},${c}`;
  }

  function fromSetKey(key) {
    return key.split(",").map(Number);
  }

  for (let c = 0; c < cols; c++) {
    pQueue.enqueue([0, c]);
    pSeen.add(toSetKey(0, c));
    aQueue.enqueue([rows - 1, c]);
    aSeen.add(toSetKey(rows - 1, c));
  }

  for (let r = 0; r < rows; r++) {
    pQueue.enqueue([r, 0]);
    pSeen.add(toSetKey(r, 0));
    aQueue.enqueue([r, cols - 1]);
    aSeen.add(toSetKey(r, cols - 1));
  }

  function bfs(queue, seen) {
    while (!queue.isEmpty()) {
      const [r, c] = queue.dequeue();

      for (const [offR, offC] of [[-1, 0], [1, 0], [0, 1], [0, -1]]) {
        const newR = r + offR;
        const newC = c + offC;

        if (
          newR >= 0 && newC >= 0 && newR < rows && newC < cols &&
          !seen.has(toSetKey(newR, newC)) &&
          heights[newR][newC] >= heights[r][c]
        ) {
          queue.enqueue([newR, newC]);
          seen.add(toSetKey(newR, newC));
        }
      }
    }
  }

  bfs(pQueue, pSeen);
  bfs(aQueue, aSeen);

  return Array.from(pSeen.intersection(aSeen)).map(fromSetKey);
};
