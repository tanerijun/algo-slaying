class _Node {
  val: number;
  neighbors: _Node[];

  constructor(val?: number, neighbors?: _Node[]) {
    this.val = val === undefined ? 0 : val;
    this.neighbors = neighbors === undefined ? [] : neighbors;
  }
}

// Time complexity: O(E+V)
// Space complexity: O(E+V)
function cloneGraph(node: _Node | null): _Node | null {
  if (!node) return null;

  const oldToNew = new Map<_Node, _Node>();

  function dfs(node: _Node): _Node {
    if (oldToNew.has(node)) {
      return oldToNew.get(node)!;
    }

    const copy = new _Node(node.val);
    oldToNew.set(node, copy);

    for (const neighbor of node.neighbors) {
      copy.neighbors.push(dfs(neighbor));
    }

    return copy;
  }

  return dfs(node);
}
