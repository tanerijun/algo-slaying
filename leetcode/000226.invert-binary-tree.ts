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

// DFS
function invertTree(root: TreeNode | null): TreeNode | null {
	if (!root) {
		return null
	}

	const left = invertTree(root.left)
	const right = invertTree(root.right)

	root.left = right
	root.right = left

	return root
}
// Time complexity: O(n)
// Space complexity: O(n)

class Queue {
	private queue: TreeNode[] = []

	constructor(initialItem?: TreeNode) {
		if (initialItem) {
			this.queue = [initialItem]
		}
	}

	enqueue(item: TreeNode) {
		this.queue.push(item)
	}

	dequeue() {
		if (this.isEmpty()) {
			throw new Error("Queue is empty")
		}

		return this.queue.shift() as TreeNode
	}

	isEmpty() {
		return this.queue.length === 0
	}
}

// BFS
function invertTreeBFS(root: TreeNode | null): TreeNode | null {
	if (!root) {
		return null
	}

	const queue = new Queue(root)

	while (!queue.isEmpty()) {
		const cur = queue.dequeue()
		const temp = cur.right
		cur.right = cur.left
		cur.left = temp

		if (cur.right) {
			queue.enqueue(cur.right)
		}

		if (cur.left) {
			queue.enqueue(cur.left)
		}
	}

	return root
}
// Time complexity: O(n)
// Space complexity: O(n)
