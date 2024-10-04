class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

class MyCircularQueue {
  size: number;
  maxSize: number;
  head: ListNode | null;
  tail: ListNode | null;

  constructor(k: number) {
    this.size = 0;
    this.maxSize = k;
    this.head = null;
    this.tail = null;
  }

  enQueue(value: number): boolean {
    if (this.isFull()) {
      return false;
    }

    if (this.size === 0) {
      this.head = new ListNode(value);
      this.tail = this.head;
    } else {
      this.tail = this.tail as ListNode;
      this.tail.next = new ListNode(value, this.head);
      this.tail = this.tail.next;
    }

    this.size++;

    return true;
  }

  deQueue(): boolean {
    if (this.isEmpty()) {
      return false;
    }

    this.size--;

    if (this.size === 0) {
      this.head = null;
      this.tail = null;
    } else {
      this.head = this.head as ListNode;
      this.tail = this.tail as ListNode;
      this.head = this.head.next;
      this.tail.next = this.head;
    }

    return true;
  }

  Front(): number {
    if (this.isEmpty()) {
      return -1;
    }

    this.head = this.head as ListNode;

    return this.head.val;
  }

  Rear(): number {
    if (this.isEmpty()) {
      return -1;
    }

    this.tail = this.tail as ListNode;

    return this.tail.val;
  }

  isEmpty(): boolean {
    return this.size === 0;
  }

  isFull(): boolean {
    return this.size === this.maxSize;
  }
}
// Time complexity of all operations: O(1)
// Space complexity: O(k) - k equals the value passed to constructor

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * var obj = new MyCircularQueue(k)
 * var param_1 = obj.enQueue(value)
 * var param_2 = obj.deQueue()
 * var param_3 = obj.Front()
 * var param_4 = obj.Rear()
 * var param_5 = obj.isEmpty()
 * var param_6 = obj.isFull()
 */
