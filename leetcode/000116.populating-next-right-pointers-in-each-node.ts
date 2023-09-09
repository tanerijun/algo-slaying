/**
 * Definition for Node.
 * class Node {
 *     val: number
 *     left: Node | null
 *     right: Node | null
 *     next: Node | null
 *     constructor(val?: number, left?: Node, right?: Node, next?: Node) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

export {};

class Node {
	val: number;
	left: Node | null;
	right: Node | null;
	next: Node | null;
	constructor(val?: number, left?: Node, right?: Node, next?: Node) {
		this.val = val === undefined ? 0 : val;
		this.left = left === undefined ? null : left;
		this.right = right === undefined ? null : right;
		this.next = next === undefined ? null : next;
	}
}

function connect(root: Node | null): Node | null {
	let curr = root;
	let next = curr?.left ? curr.left : null; // pointer to the next level

	while (curr && next) {
		// Connect childs
		curr.left!.next = curr.right;

		// If the current node is connected to a different node,
		// the right child of the current node should point to the left child of the node it's connected to.
		if (curr.next) {
			curr.right!.next = curr.next.left;
		}

		curr = curr.next;

		if (!curr) {
			// Proceed to the next level
			curr = next;
			next = curr.left;
		}
	}

	return root;
}
// Time complexity: O(n)
// Space complexity: O(1)
