class MaxHeap {
  private heap: number[];

  constructor(arr: number[] = []) {
    this.heap = arr;
    if (this.heap.length > 0) {
      this.buildHeap();
    }
  }

  size(): number {
    return this.heap.length;
  }

  peek(): number {
    return this.heap[0];
  }

  push(val: number) {
    this.heap.push(val);
    this.heapifyUp(this.heap.length - 1);
  }

  pop(): number | undefined {
    if (this.heap.length === 0) return undefined;

    if (this.heap.length === 1) return this.heap.pop();

    const max = this.heap[0];
    this.heap[0] = this.heap.pop()!;
    this.heapifyDown(0);

    return max;
  }

  private buildHeap() {
    const startIndex = Math.floor(this.heap.length / 2 - 1);
    for (let i = startIndex; i >= 0; i--) {
      this.heapifyDown(i);
    }
  }

  private heapifyDown(idx: number) {
    let largest = idx;
    const left = idx * 2 + 1;
    const right = idx * 2 + 2;

    if (left < this.heap.length && this.heap[left] > this.heap[largest]) {
      largest = left;
    }
    if (right < this.heap.length && this.heap[right] > this.heap[largest]) {
      largest = right;
    }
    if (largest !== idx) {
      this.swap(idx, largest);
      this.heapifyDown(largest);
    }
  }

  private heapifyUp(idx: number) {
    if (idx === 0) return;
    const parent = Math.floor((idx - 1) / 2);
    if (this.heap[idx] > this.heap[parent]) {
      this.swap(idx, parent);
      this.heapifyUp(parent);
    }
  }

  private swap(i: number, j: number) {
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
  }
}

// Time complexity: O(n(log(n)))
// Space complexity: O(n)
function lastStoneWeight(stones: number[]): number {
  const heap = new MaxHeap(stones);
  while (heap.size() > 1) {
    const a = heap.pop()!;
    const b = heap.pop()!;
    const c = a - b;
    if (c > 0) {
      heap.push(c);
    }
  }
  return heap.size() === 0 ? 0 : heap.peek();
}
