class MyHashMap {
	// Since it's mentioned in the constraint that
	// At most 10^4 calls will be made to add, remove, and contains.
	// We can hard code it, and avoid the need to implement rehashing.
	LENGTH = 10 ** 4
	map: ListNode[] = []

	constructor() {
		this.map = new Array(this.LENGTH)
		for (let i = 0; i < this.LENGTH; i++) {
			const dummyNode = new ListNode(0, 0)
			this.map[i] = dummyNode
		}
	}

	_hash(key: number): number {
		return key % this.LENGTH
	}

	put(key: number, value: number): void {
		const index = this._hash(key)
		let cur: ListNode | null = this.map[index]

		while (cur.next) {
			if (cur.next.val[0] === key) {
				cur.next.val[1] = value
				return
			}

			cur = cur.next
		}

		cur.next = new ListNode(key, value)
	}

	get(key: number): number {
		const index = this._hash(key)
		let cur: ListNode | null = this.map[index]

		while (cur.next) {
			if (cur.next.val[0] === key) {
				return cur.next.val[1]
			}

			cur = cur.next
		}

		return -1
	}

	remove(key: number): void {
		const index = this._hash(key)
		let cur: ListNode | null = this.map[index]

		while (cur.next) {
			if (cur.next.val[0] === key) {
				if (cur.next.next) {
					cur.next = cur.next.next
					return
				}

				cur.next = null
				return
			}

			cur = cur.next
		}
	}
}

type KVPair = [number, number]

class ListNode {
	val: KVPair
	next: ListNode | null

	constructor(key: number, val: number) {
		this.val = [key, val]
		this.next = null
	}
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = new MyHashMap()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */

// Time complexity: O(1) on average
// Space complexity: O(n)
