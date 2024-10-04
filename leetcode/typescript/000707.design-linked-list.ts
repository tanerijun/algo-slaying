class LinkedListItem {
  constructor(public readonly val: number, public next?: LinkedListItem) {}
}

class MyLinkedList {
  private head?: LinkedListItem;

  get(index: number): number {
    let item = this.head;

    for (let i = 0; i <= index && item; i++) {
      if (i === index) {
        return item.val;
      }

      item = item.next;
    }

    return -1;
  }

  addAtHead(val: number): void {
    this.head = new LinkedListItem(val, this.head);
  }

  addAtTail(val: number): void {
    if (!this.head) {
      return this.addAtHead(val);
    }

    let lastItem = this.head;

    while (lastItem.next) {
      lastItem = lastItem.next;
    }

    lastItem.next = new LinkedListItem(val);
  }

  addAtIndex(index: number, val: number): void {
    if (!index) {
      return this.addAtHead(val);
    }

    let item = this.head;

    for (let i = 0; i <= index - 1 && item; i++) {
      if (i === index - 1) {
        item.next = new LinkedListItem(val, item.next);

        return;
      }

      item = item.next;
    }
  }

  deleteAtIndex(index: number): void {
    if (!index) {
      this.head = this.head?.next;

      return;
    }

    let item = this.head;

    for (let i = 0; i <= index - 1 && item; i++) {
      if (i === index - 1) {
        item.next = item.next?.next;

        return;
      }

      item = item.next;
    }
  }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * var obj = new MyLinkedList()
 * var param_1 = obj.get(index)
 * obj.addAtHead(val)
 * obj.addAtTail(val)
 * obj.addAtIndex(index,val)
 * obj.deleteAtIndex(index)
 */
