class ListNode {
	val: number
	next: ListNode | null
	constructor(val?: number, next?: ListNode | null) {
		this.val = val === undefined ? 0 : val
		this.next = next === undefined ? null : next
	}
}

function middleNode(head: ListNode | null): ListNode | null {
	const temp: ListNode[] = []

	while (head !== null) {
		temp.push(head)
		head = head.next
	}

	const midNodeIdx = Math.floor(temp.length / 2)

	return temp[midNodeIdx]
}
// Time complexity: O(n) - where `n` equals the length of the linked list
// Space complexity: O(n)

function middleNode2(head: ListNode | null): ListNode | null {
	// 2 pointers
	// If you try drawing linked list of several length,
	// you'll notice a pattern:
	// The index of mid node increases by 1,
	// everytime the length of the list increase by 2.
	let mid = head
	let end = head

	while (end !== null && end.next !== null) {
		mid = mid!.next // because `mid` is always behind `end`, it can't possibly be null
		end = end.next.next
	}

	return mid
}
// Time complexity: O(n)
// Space complexity: O(1)
