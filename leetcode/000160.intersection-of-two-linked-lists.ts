class ListNode {
	val: number;
	next: ListNode | null;
	constructor(val?: number, next?: ListNode | null) {
		this.val = val === undefined ? 0 : val;
		this.next = next === undefined ? null : next;
	}
}

function getIntersectionNode(headA: ListNode | null, headB: ListNode | null): ListNode | null {
	const set = new Set<ListNode>();
	let cur = headA;

	while (cur) {
		set.add(cur);
		cur = cur.next;
	}

	cur = headB;

	while (cur) {
		if (set.has(cur)) {
			return cur;
		}

		cur = cur.next;
	}

	return null;
}
// Time complexity: O(m + n)
// Space complexity: O(m)

function getIntersectionNode2(headA: ListNode | null, headB: ListNode | null): ListNode | null {
	let lengthA = 0;
	let curA = headA;

	while (curA) {
		lengthA++;
		curA = curA.next;
	}

	let lengthB = 0;
	let curB = headB;

	while (curB) {
		lengthB++;
		curB = curB.next;
	}

	// Now that we have the length of each list, reset the pointers
	curA = headA;
	curB = headB;

	// We're going to traverse through the list again, but this time with the same start
	if (lengthA > lengthB) {
		const offset = lengthA - lengthB;

		for (let i = 0; i < offset; i++) {
			curA = curA?.next || null;
		}
	} else if (lengthB > lengthA) {
		const offset = lengthB - lengthA;

		for (let i = 0; i < offset; i++) {
			curB = curB?.next || null;
		}
	}

	while (curA && curB) {
		if (curA === curB) {
			return curA;
		}

		curA = curA.next;
		curB = curB.next;
	}

	return null;
}
// Time complexity: O(m + n)
// Space complexity: O(1)

function getIntersectionNode3(headA: ListNode | null, headB: ListNode | null): ListNode | null {
	let curA = headA;
	let curB = headB;

	// They'll eventually intersect, worst case is at null (try drawing)
	while (curA !== curB) {
		curA = curA ? curA.next : headB;
		curB = curB ? curB.next : headA;
	}

	return curA;
}
// Time complexity: O(m + n)
// Space complexity: O(1)
