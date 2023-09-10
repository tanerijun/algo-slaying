class ListNode {
	val: number;
	next: ListNode | null;
	constructor(val?: number, next?: ListNode | null) {
		this.val = val === undefined ? 0 : val;
		this.next = next === undefined ? null : next;
	}
}

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
	const dummyHead = new ListNode();
	let curr: ListNode | null = dummyHead;

	while (list1 && list2) {
		if (list1.val <= list2.val) {
			curr.next = list1;
			list1 = list1.next;
		} else {
			curr.next = list2;
			list2 = list2.next;
		}

		curr = curr.next;
	}

	// At this point, one of the list is empty,
	// and we need to plug the rest of the elements in the other list to our answer list.
	curr.next = list1 === null ? list2 : list1;

	return dummyHead.next;
}
// Time complexity: O(n)
// Space complexity: O(1)
