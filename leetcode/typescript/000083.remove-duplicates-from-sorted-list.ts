class ListNode {
	val: number;
	next: ListNode | null;
	constructor(val?: number, next?: ListNode | null) {
		this.val = val === undefined ? 0 : val;
		this.next = next === undefined ? null : next;
	}
}

function deleteDuplicates(head: ListNode | null): ListNode | null {
	const dummyHead = new ListNode(Number.MIN_SAFE_INTEGER, head);
	let prev: ListNode | null = dummyHead;
	let cur: ListNode | null = head;

	while (cur) {
		if (cur.val === prev.val) {
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

function deleteDuplicates2(head: ListNode | null): ListNode | null {
	let cur: ListNode | null = head;

	while (cur) {
		while (cur.next && cur.next.val === cur.val) {
			cur.next = cur.next.next;
		}

		cur = cur.next;
	}

	return head;
}
