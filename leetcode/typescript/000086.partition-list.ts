class ListNode {
	val: number
	next: ListNode | null
	constructor(val?: number, next?: ListNode | null) {
		this.val = val === undefined ? 0 : val
		this.next = next === undefined ? null : next
	}
}

function partition(head: ListNode | null, x: number): ListNode | null {
	const dummyLeft = new ListNode(0)
	const dummyRight = new ListNode(0)
	let cur = head
	let curLeft = dummyLeft
	let curRight = dummyRight

	while (cur) {
		if (cur.val < x) {
			curLeft.next = cur
			curLeft = curLeft.next
		} else {
			curRight.next = cur
			curRight = curRight.next
		}

		cur = cur.next
	}

	curRight.next = null
	curLeft.next = dummyRight.next

	return dummyLeft.next
}
// Time complexity: O(n)
// Space complexity: O(1)
