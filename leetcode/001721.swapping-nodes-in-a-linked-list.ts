class ListNode {
	val: number;
	next: ListNode | null;
	constructor(val?: number, next?: ListNode | null) {
		this.val = val === undefined ? 0 : val;
		this.next = next === undefined ? null : next;
	}
}

function swapNodes(head: ListNode | null, k: number): ListNode | null {
	let fast = head;
	let slow = head;

	for (let i = 1; i < k; i++) {
		if (fast) {
			fast = fast.next;
		} else {
			break;
		}
	}

	const kFirstNode = fast as ListNode;

	while (fast && fast.next) {
		fast = fast.next;
		slow = slow!.next;
	}

	const kLastNode = slow as ListNode;
	const temp = kFirstNode.val;
	kFirstNode.val = kLastNode.val;
	kLastNode.val = temp;

	return head;
}
// Time complexity: O(n)
// Space complexity: O(1)
