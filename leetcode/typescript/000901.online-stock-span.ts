class StockSpanner {
  stack: Array<{ price: number; span: number }>;

  constructor() {
    this.stack = [];
  }

  top() {
    return this.stack[this.stack.length - 1];
  }

  isEmpty() {
    return this.stack.length === 0;
  }

  next(price: number): number {
    const stock = { price, span: 1 };

    while (!this.isEmpty() && price >= this.top().price) {
      const popped = this.stack.pop();
      stock.span += popped!.span;
    }

    this.stack.push(stock);

    return this.top().span;
  }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * var obj = new StockSpanner()
 * var param_1 = obj.next(price)
 */

// Time complexity of the 'next' method: O(n)
// Space complexity of the 'next' method: O(n)
