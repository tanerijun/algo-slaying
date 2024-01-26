class ListNode {
	val: number
	next: ListNode | null
	constructor(val?: number, next?: ListNode | null) {
		this.val = val === undefined ? 0 : val
		this.next = next === undefined ? null : next
	}
}

function rotateRight(head: ListNode | null, k: number): ListNode | null {
	if (!head || k === 0) {
		return head
	}

	let count = 0
	let cur: ListNode | null = head

	while (cur && cur.next) {
		count++
		cur = cur.next
	}

	count++
	cur!.next = head // connect list
	cur = head

	for (let i = 1; i < count - (k % count); i++) {
		cur = cur!.next
	}

	const newHead = cur!.next
	cur!.next = null // disconnect last node

	return newHead
}
// Time complexity: O(n)
// Space complexity: O(1)
