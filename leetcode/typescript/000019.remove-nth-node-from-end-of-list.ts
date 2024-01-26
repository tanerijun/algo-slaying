class ListNode {
	val: number;
	next: ListNode | null;
	constructor(val?: number, next?: ListNode | null) {
		this.val = val === undefined ? 0 : val;
		this.next = next === undefined ? null : next;
	}
}

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
	if (!head) return null;

	let fast: ListNode | null = head;
	let slow: ListNode | null = head;

	for (let i = 0; i < n; i++) {
		if (fast) {
			fast = fast.next;
		} else {
			break;
		}
	}

	// Edge case: n = size of the list, removing the last item in the list
	if (!fast) {
		return head.next;
	}

	while (fast.next) {
		fast = fast.next;
		slow = slow!.next;
	}

	// At this point, fast will be at the end of the list,
	// and slow will be pointing to the element to be removed
	slow = slow as ListNode; // both slow and slow.next is behind fast. So if fast is not null, they can't be null
	const temp = slow.next as ListNode;
	slow.next = temp.next;
	temp.next = null;

	return head;
}
