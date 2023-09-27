class ListNode {
	val: number
	next: ListNode | null
	constructor(val?: number, next?: ListNode | null) {
		this.val = val === undefined ? 0 : val
		this.next = next === undefined ? null : next
	}
}

function reverseBetween(head: ListNode | null, left: number, right: number): ListNode | null {
	if (!head || left === right) {
		return head
	}

	let beforeFirst: ListNode | null = null
	let first: ListNode | null = null
	let last: ListNode | null = null
	let cur: ListNode | null = head
	let count = 1

	while (cur) {
		if (count === left - 1) {
			beforeFirst = cur
		} else if (count === left) {
			first = cur
		} else if (count === right) {
			last = cur
			break
		}

		cur = cur.next
		count++
	}

	// Constraint: 1 <= left <= right <= n
	cur = first
	let prev = last!.next

	if (beforeFirst) {
		beforeFirst.next = last
	}

	for (let i = 0; i < right - left + 1; i++) {
		const tmp = cur!.next
		cur!.next = prev
		prev = cur
		cur = tmp
	}

	return head
}
// Time complexity: O(n)
// Space complexity: O(1)
