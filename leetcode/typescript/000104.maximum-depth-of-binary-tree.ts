class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

// Recursive DFS
function maxDepth(root: TreeNode | null): number {
  if (!root) {
    return 0;
  }

  return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}
// Time complexity: O(n)
// Space complexity: O(n)

// Iterative BFS
class TreeNodeQueue {
  private queue: TreeNode[] = [];

  constructor(item?: TreeNode) {
    if (item) {
      this.queue.push(item);
    }
  }

  enqueue(item: TreeNode) {
    this.queue.push(item);
  }

  dequeue() {
    if (this.isEmpty()) {
      throw new Error("Queue is empty");
    }

    return this.queue.shift() as TreeNode;
  }

  isEmpty() {
    return this.queue.length === 0;
  }

  get length() {
    return this.queue.length;
  }
}

function maxDepthBFS(root: TreeNode | null): number {
  if (!root) {
    return 0;
  }

  let level = 0;
  const queue = new TreeNodeQueue(root);

  while (!queue.isEmpty()) {
    const levelSize = queue.length;

    // Empty current queue
    for (let i = 0; i < levelSize; i++) {
      const cur = queue.dequeue();

      // Add all it's children back to the queue
      if (cur.left) {
        queue.enqueue(cur.left);
      }

      if (cur.right) {
        queue.enqueue(cur.right);
      }
    }

    level++;
  }

  return level;
}
// Time complexity: O(n)
// Space complexity: O(n)

// Iterative DFS
function maxDepthDFSIterative(root: TreeNode | null): number {
  const stack: Array<[TreeNode | null, number]> = [[root, 1]];
  let res = 1;

  while (stack.length > 0) {
    const [node, level] = stack.pop()!;

    if (node) {
      res = Math.max(res, level);
      stack.push([node.left, level + 1]);
      stack.push([node.right, level + 1]);
    }
  }

  return res;
}
// Time complexity: O(n)
// Space complexity: O(n)
