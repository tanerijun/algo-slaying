// Definition for singly-linked list.
export class ListNode {
	val: number;
	next: ListNode | null;
	constructor(val?: number, next?: ListNode | null) {
		this.val = val === undefined ? 0 : val;
		this.next = next === undefined ? null : next;
	}
}

export function addTwoNumbers(
	l1: ListNode | null,
	l2: ListNode | null,
): ListNode | null {
	const answerHead = new ListNode();
	let cursor = answerHead;
	let carry = 0;

	while (l1 !== null || l2 !== null) {
		const x = l1 ? l1.val : 0;
		const y = l2 ? l2.val : 0;
		const sum = x + y + carry;
		carry = sum >= 10 ? 1 : 0;
		cursor.next = new ListNode(sum % 10);
		cursor = cursor.next;

		if (l1 != null) l1 = l1.next;
		if (l2 != null) l2 = l2.next;
	}

	if (carry > 0) {
		cursor.next = new ListNode(carry);
	}

	return answerHead.next;
}
