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
function postorderTraversal(root: TreeNode | null): number[] {
	const res: number[] = []

	function walk(node: TreeNode | null) {
		if (node) {
			walk(node.left)
			walk(node.right)
			res.push(node.val)
		}
	}

	walk(root)

	return res
}
// Time complexity: O(n)
// Space complexity: O(n)

// Iterative with stack
function postorderTraversalIterative(root: TreeNode | null): number[] {
	const res: number[] = []
	const stack: Array<TreeNode | null> = [root]
	const visited: boolean[] = [false]

	while (stack.length > 0) {
		const cur = stack.pop()
		const isVisited = visited.pop()

		if (cur) {
			if (isVisited) {
				res.push(cur.val)
			} else {
				stack.push(cur)
				visited.push(true)

				stack.push(cur.right)
				visited.push(false)

				stack.push(cur.left)
				visited.push(false)
			}
		}
	}

	return res
}
// Time complexity: O(n)
// Space complexity: O(n)
