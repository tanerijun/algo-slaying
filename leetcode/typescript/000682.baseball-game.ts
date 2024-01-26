function calPoints(operations: string[]): number {
	const stack: number[] = [];

	for (const operation of operations) {
		switch (operation) {
			case "C":
				stack.pop();
				break;
			case "D":
				stack.push(stack[stack.length - 1] * 2);
				break;
			case "+":
				stack.push(stack[stack.length - 1] + stack[stack.length - 2]);
				break;
			default:
				stack.push(parseInt(operation));
		}
	}

	return stack.length ? stack.reduce((a, b) => a + b) : 0;
}
// Time complexity: O(n)
// Space complexity: O(n)
