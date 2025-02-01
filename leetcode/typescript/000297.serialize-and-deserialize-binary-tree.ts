/**
 * Definition for a binary tree node.
 */
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

/*
 * Encodes a tree to a single string.
 */
function serialize(root: TreeNode | null): string {
  const res: Array<"N" | number> = [];

  function dfs(node: TreeNode | null): void {
    if (!node) {
      res.push("N");
      return;
    }
    res.push(node.val);
    dfs(node.left);
    dfs(node.right);
  }

  dfs(root);
  return res.join(",");
}

/*
 * Decodes your encoded data to tree.
 */
function deserialize(data: string): TreeNode | null {
  const values = data.split(",");
  let i: number = 0;

  function dfs() {
    if (values[i] === "N") {
      i++;
      return null;
    }
    const node = new TreeNode(Number(values[i]));
    i++;
    node.left = dfs();
    node.right = dfs();
    return node;
  }

  return dfs();
}

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */
