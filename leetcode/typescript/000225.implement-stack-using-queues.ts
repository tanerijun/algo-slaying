class MyStack {
	_stack: number[];

	constructor() {
		this._stack = [];
	}

	push(x: number): void {
		this._stack.push(x);
	}

	pop(): number {
		if (!this._stack.length) {
			throw new Error("Stack is empty");
		}

		return this._stack.pop()!;
	}

	top(): number {
		return this._stack[this._stack.length - 1];
	}

	empty(): boolean {
		return this._stack.length === 0;
	}
}

/**
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */
