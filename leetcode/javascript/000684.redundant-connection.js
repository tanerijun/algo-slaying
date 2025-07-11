/**
 * @param {number[][]} edges
 * @return {number[]}
 * Time complexity: O(V + E), Since count(V) == count(E) in this case, tc becomes O(n)
 * Space complexity: O(n)
 */
var findRedundantConnection = function (edges) {
  const parents = Array.from({ length: edges.length + 1 }, (_, i) => i); // each node has itself as its parent
  const ranks = Array(edges.length + 1).fill(1); // every node starts off as rank 1

  // Return the root parent of a node,
  // while also doing path compressing at the same time
  function find(n) {
    if (n !== parents[n]) {
      parents[n] = find(parents[n]);
    }
    return parents[n];
  }

  // An uncomplete union algorithm for this specific problem
  // Return true if connection is successfully made (no cycle)
  // and vice versa
  function union(n1, n2) {
    const parent1 = find(n1);
    const parent2 = find(n2);

    // Cycle detected
    if (parent1 === parent2) {
      return false;
    }

    // No cycle -> connect nodes -> node with higher rank should be the parent
    if (ranks[parent1] > ranks[parent2]) {
      parents[parent2] = parent1;
      ranks[parent1] += ranks[parent2];
    } else {
      parents[parent1] = parent2;
      ranks[parent2] += ranks[parent1];
    }

    return true;
  }

  // Check each edge for cycle
  // The problem states that exactly 1 extra edge exist
  // So there's no need to handle the false case
  for (const [n1, n2] of edges) {
    if (!union(n1, n2)) {
      return [n1, n2];
    }
  }
};
