class Heap<T> {
  private heap: T[];
  private compare: (a: T, b: T) => number;

  constructor(compareFn: (a: T, b: T) => number, arr: T[] = []) {
    this.heap = arr;
    this.compare = compareFn;
    if (this.heap.length > 0) {
      this.buildHeap();
    }
  }

  public size(): number {
    return this.heap.length;
  }

  public peek(): T | undefined {
    return this.heap[0];
  }

  public push(value: T): void {
    this.heap.push(value);
    this.heapifyUp(this.heap.length - 1);
  }

  public pop(): T | undefined {
    if (this.heap.length === 0) {
      return undefined;
    }

    if (this.heap.length === 1) {
      return this.heap.pop();
    }

    const result = this.heap[0];
    this.heap[0] = this.heap.pop()!;
    this.heapifyDown(0);

    return result;
  }

  private buildHeap(): void {
    const startIndex = Math.floor(this.heap.length / 2 - 1);
    for (let i = startIndex; i >= 0; i--) {
      this.heapifyDown(i);
    }
  }

  private heapifyDown(index: number): void {
    let current = index;
    const leftChild = 2 * index + 1;
    const rightChild = 2 * index + 2;

    if (
      leftChild < this.heap.length &&
      this.compare(this.heap[leftChild], this.heap[current]) < 0
    ) {
      current = leftChild;
    }

    if (
      rightChild < this.heap.length &&
      this.compare(this.heap[rightChild], this.heap[current]) < 0
    ) {
      current = rightChild;
    }

    if (current !== index) {
      this.swap(index, current);
      this.heapifyDown(current);
    }
  }

  private heapifyUp(index: number): void {
    if (index === 0) return;

    const parent = Math.floor((index - 1) / 2);
    if (this.compare(this.heap[index], this.heap[parent]) < 0) {
      this.swap(index, parent);
      this.heapifyUp(parent);
    }
  }

  private swap(i: number, j: number): void {
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
  }
}

class MedianFinder {
  private minHeap: Heap<number>;
  private maxHeap: Heap<number>;

  constructor() {
    this.minHeap = new Heap<number>((a, b) => a - b);
    this.maxHeap = new Heap<number>((a, b) => b - a);
  }

  // Time complexity: O(log(n))
  addNum(num: number): void {
    this.maxHeap.push(num);

    const maxHeapTop = this.maxHeap.peek();
    const minHeapTop = this.minHeap.peek();
    if (maxHeapTop && minHeapTop && maxHeapTop > minHeapTop) {
      this.maxHeap.pop();
      this.minHeap.push(maxHeapTop);
    }

    if (this.maxHeap.size() > this.minHeap.size()) {
      const maxHeapTop = this.maxHeap.pop()!;
      this.minHeap.push(maxHeapTop);
    }

    if (this.minHeap.size() > this.maxHeap.size()) {
      const minHeapTop = this.minHeap.pop()!;
      this.maxHeap.push(minHeapTop);
    }
  }

  // Time complexity: O(1)
  findMedian(): number {
    if (this.maxHeap.size() === this.minHeap.size()) {
      const maxHeapTop = this.maxHeap.peek();
      const minHeapTop = this.minHeap.peek();

      if (maxHeapTop !== undefined && minHeapTop !== undefined) {
        return (maxHeapTop + minHeapTop) / 2;
      } else {
        throw new Error(
          "There should be at least one element in the data structure",
        );
      }
    }

    return this.maxHeap.size() > this.minHeap.size()
      ? this.maxHeap.peek()!
      : this.minHeap.peek()!;
  }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = new MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */
