class ListNode {
	val: number;
	next: ListNode | null;
	constructor(val?: number, next?: ListNode | null) {
		this.val = val === undefined ? 0 : val;
		this.next = next === undefined ? null : next;
	}
}

function removeElements(head: ListNode | null, val: number): ListNode | null {
	const dummyHead = new ListNode(0, head);
	let prev = dummyHead;
	let cur = head;

	while (cur) {
		if (cur.val === val) {
			prev.next = cur.next;
		} else {
			prev = cur;
		}

		cur = cur.next;
	}

	return dummyHead.next;
}
// Time complexity: O(n)
// Space complexity: O(1)
