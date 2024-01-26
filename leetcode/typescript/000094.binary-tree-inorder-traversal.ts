class TreeNode {
	val: number
	left: TreeNode | null
	right: TreeNode | null
	constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
		this.val = val === undefined ? 0 : val
		this.left = left === undefined ? null : left
		this.right = right === undefined ? null : right
	}
}

// Recursive
function inorderTraversal(root: TreeNode | null): number[] {
	const res: number[] = []

	function walk(node: TreeNode | null) {
		if (node) {
			walk(node.left)
			res.push(node.val)
			walk(node.right)
		}
	}

	walk(root)

	return res
}
// Time complexity: O(n)
// Space complexity: O(n)

// Imperative using stack
function inorderTraversalWithStack(root: TreeNode | null): number[] {
	const res: number[] = []
	const stack: TreeNode[] = []
	let curr = root

	while (curr || !(stack.length === 0)) {
		while (curr) {
			stack.push(curr)
			curr = curr.left
		}

		curr = stack.pop()!
		res.push(curr.val)
		curr = curr.right
	}

	return res
}
// Time complexity: O(n)
// Space complexity: O(n)
