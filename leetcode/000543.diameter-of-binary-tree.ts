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

function diameterOfBinaryTree(root: TreeNode | null): number {
	let maxDiameter = 0

	function dfs(root: TreeNode | null) {
		if (!root) {
			return -1
		}

		const left = dfs(root.left)
		const right = dfs(root.right)

		maxDiameter = Math.max(maxDiameter, left + right + 1 + 1) // Height of left subtree + height of right subtree + 1 to cancel -1 height for null node + 1 for current node

		return 1 + Math.max(left, right)
	}

	dfs(root)

	return maxDiameter
}
// Time complexity: O(n)
// Space complexity: O(n)
