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
function preorderTraversal(root: TreeNode | null): number[] {
	const res: number[] = []

	function walk(node: TreeNode | null) {
		if (node) {
			res.push(node.val)
			walk(node.left)
			walk(node.right)
		}
	}

	walk(root)

	return res
}
// Time complexity: O(n)
// Space complexity: O(n)
