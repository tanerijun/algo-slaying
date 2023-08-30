function removeDuplicates(s: string, k: number): string {
	const stack: Array<[string, number]> = [];

	for (const c of s) {
		if (stack.length === 0 || !(stack[stack.length - 1][0] === c)) {
			stack.push([c, 1]);
		} else {
			stack[stack.length - 1][1]++;
		}

		if (stack[stack.length - 1][1] === k) {
			stack.pop();
		}
	}

	let res = "";
	for (let i = 0; i < stack.length; i++) {
		for (let j = 0; j < stack[i][1]; j++) {
			res += stack[i][0];
		}
	}

	return res;
}
// Time complexity: O(n)
// Space complexity: O(n)
