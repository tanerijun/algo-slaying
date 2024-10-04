class LNode {
  key: number;
  val: number;
  prev: LNode | null = null;
  next: LNode | null = null;

  constructor(k: number, v: number) {
    this.key = k;
    this.val = v;
  }
}

class LRUCache {
  map = new Map<number, LNode>();
  size: number;
  head: LNode;
  tail: LNode;

  constructor(capacity: number) {
    this.size = capacity;

    // Dummy nodes
    this.head = new LNode(0, 0);
    this.tail = new LNode(0, 0);

    // Connect nodes
    this.head.next = this.tail;
    this.tail.prev = this.head;
  }

  get(key: number): number {
    const node = this.map.get(key);

    // Cache miss
    if (!node) {
      return -1;
    }

    this.removeNode(node);
    this.addNode(node);

    return node.val;
  }

  put(key: number, value: number): void {
    let node = this.map.get(key);

    if (node) {
      this.removeNode(node);
    }

    node = new LNode(key, value);

    this.addNode(node);

    // Remove least used node on full capacity
    if (this.map.size > this.size) {
      this.removeNode(this.tail.prev!);
    }
  }

  private removeNode(node: LNode) {
    // Only head and tail have one side that's null
    node.prev!.next = node.next;
    node.next!.prev = node.prev;

    this.map.delete(node.key);
  }

  private addNode(node: LNode) {
    node.prev = this.head;
    node.next = this.head.next;
    this.head.next!.prev = node;
    this.head.next = node;

    this.map.set(node.key, node);
  }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
