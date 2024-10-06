class MinHeap {
  private heap: number[];

  constructor(arr: number[] = []) {
    this.heap = arr;
    if (this.heap.length > 0) {
      this.buildHeap();
    }
  }

  // O(1)
  size(): number {
    return this.heap.length;
  }

  // O(1)
  peek(): number | undefined {
    return this.heap.length > 0 ? this.heap[0] : undefined;
  }

  // O(log(n))
  push(val: number) {
    this.heap.push(val);
    this.heapifyUp(this.heap.length - 1);
  }

  // O(log(n))
  pop(): number | undefined {
    if (this.heap.length === 0) {
      return undefined;
    }

    if (this.heap.length === 1) {
      return this.heap.pop();
    }

    const min = this.heap[0];
    this.heap[0] = this.heap.pop()!;
    this.heapifyDown(0);

    return min;
  }

  // O(n)
  private buildHeap() {
    const startIndex = Math.floor(this.heap.length / 2 - 1); // last non-leaf node
    for (let i = startIndex; i >= 0; i--) {
      this.heapifyDown(i);
    }
  }

  // O(log(n))
  private heapifyDown(idx: number) {
    let smallest = idx;
    const left = idx * 2 + 1;
    const right = idx * 2 + 2;

    if (left < this.heap.length && this.heap[left] < this.heap[smallest]) {
      smallest = left;
    }
    if (right < this.heap.length && this.heap[right] < this.heap[smallest]) {
      smallest = right;
    }
    if (smallest !== idx) {
      this.swap(idx, smallest);
      this.heapifyDown(smallest);
    }
  }

  // O(log(n))
  private heapifyUp(idx: number) {
    if (idx === 0) return;
    const parent = Math.floor((idx - 1) / 2);
    if (this.heap[idx] < this.heap[parent]) {
      this.swap(idx, parent);
      this.heapifyUp(parent);
    }
  }

  // O(1)
  private swap(i: number, j: number) {
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
  }
}

class KthLargest {
  minHeap: MinHeap;
  k: number;

  // O(n*log(n))
  constructor(k: number, nums: number[]) {
    this.minHeap = new MinHeap(nums);
    this.k = k;

    while (this.minHeap.size() > k) {
      this.minHeap.pop();
    }
  }

  // O(log(n))
  add(val: number): number {
    this.minHeap.push(val);
    if (this.minHeap.size() > this.k) {
      this.minHeap.pop();
    }

    return this.minHeap.peek()!;
  }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * var obj = new KthLargest(k, nums)
 * var param_1 = obj.add(val)
 */
