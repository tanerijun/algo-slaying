class MyHashSet {
  // Since it's mentioned in the constraint that
  // At most 10^4 calls will be made to add, remove, and contains.
  // We can hard code it, and avoid the need to implement rehashing.
  LENGTH = 10 ** 4;
  set: ListNode[] = [];

  constructor() {
    this.set = new Array(this.LENGTH);
    for (let i = 0; i < this.LENGTH; i++) {
      const dummyNode = new ListNode(0);
      this.set[i] = dummyNode;
    }
  }

  _hash(key: number): number {
    return key % this.LENGTH;
  }

  add(key: number): void {
    const index = this._hash(key);
    let listHead = this.set[index];

    // Traverse the linkedList, returning early if duplicate found
    while (listHead.next !== null) {
      if (listHead.next.val === key) {
        return;
      }

      listHead = listHead.next;
    }

    listHead.next = new ListNode(key);
  }

  remove(key: number): void {
    const index = this._hash(key);
    let listHead = this.set[index];

    // Traverse the linkedList to find the key, then remove it
    while (listHead.next !== null) {
      if (listHead.next.val === key) {
        listHead.next = listHead.next.next;
        return;
      }

      listHead = listHead.next;
    }
  }

  contains(key: number): boolean {
    const index = this._hash(key);
    let listHead = this.set[index];

    // Traverse the listHead, returning early if duplicate found
    while (listHead.next !== null) {
      if (listHead.next.val === key) {
        return true;
      }

      listHead = listHead.next;
    }

    return false;
  }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * var obj = new MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * var param_3 = obj.contains(key)
 */

class ListNode {
  val: number | null;
  next: ListNode | null;

  constructor(val: number) {
    this.val = val;
    this.next = null;
  }
}

// Time complexity: O(1) in average case
// Space complexity: O(n)
