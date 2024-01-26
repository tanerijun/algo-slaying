class ListNode {
	val: number;
	next: ListNode | null;
	constructor(val?: number, next?: ListNode | null) {
		this.val = val === undefined ? 0 : val;
		this.next = next === undefined ? null : next;
	}
}

function pairSum(head: ListNode | null): number {
	let fast = head;
	let slow = head;

	while (fast && fast.next) {
		fast = fast.next.next;
		slow = slow!.next;
	}

	let curA = head;
	let curB = reverse(slow);
	let max = 0;

	while (curA && curB) {
		max = Math.max(curA.val + curB.val, max);
		curA = curA.next;
		curB = curB.next;
	}

	return max;
}
// Time complexity: O(n)
// Space complexity: O(1)

function reverse(head: ListNode | null): ListNode | null {
	let prev: ListNode | null = null;
	let cur = head;

	while (cur) {
		const temp = cur.next;
		cur.next = prev;
		prev = cur;
		cur = temp;
	}

	return prev;
}
