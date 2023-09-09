/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

class ListNode {
	val: number;
	next: ListNode | null;
	constructor(val?: number, next?: ListNode | null) {
		this.val = val === undefined ? 0 : val;
		this.next = next === undefined ? null : next;
	}
}

function reverseList(head: ListNode | null): ListNode | null {
	if (!head) {
		return null;
	}

	let curr: ListNode | null = head;
	let tailNode = new ListNode();

	while (curr) {
		tailNode.val = curr.val;

		if (curr.next) {
			const newTailNode = new ListNode(undefined, tailNode);
			tailNode = newTailNode;
		}

		curr = curr.next;
	}

	return tailNode;
}
// Time complexity: O(n)
// Space complexity: O(1)
