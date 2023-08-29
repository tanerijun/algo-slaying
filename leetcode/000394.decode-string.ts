function decodeString(s: string): string {
	const stack: Array<string> = [];

	for (let c of s) {
		// Add everything to stack except "]"
		if (c !== "]") {
			stack.push(c);
			continue;
		}

		// Get substring up to "["
		let subStr = "";
		while (stack[stack.length - 1] !== "[") {
			subStr = stack.pop() + subStr;
		}

		// Throw away the "["
		stack.pop();

		// Get the integer in front of "[", note that it's possible for the integer to be more than 1 digit
		let n = "";
		while (/\d/.test(stack[stack.length - 1])) {
			n = stack.pop() + n;
		}

		// Push the substring back into the stack n times
		for (let i = 0, count = parseInt(n); i < count; i++) {
			stack.push(subStr);
		}
	}

	return stack.join("");
}
// Time complexity: O(n)
// Space complexity: O(n)
