function removeKdigits(num: string, k: number): string {
	const stack: string[] = [];

	// Edge case
	if (num.length === k) {
		return "0";
	}

	let i = 0;
	while (i < num.length && k > 0) {
		// Our stack should be in monotonic increasing order
		if (stack.length === 0 || stack[stack.length - 1] <= num[i]) {
			stack.push(num[i]);
			i++;
			continue;
		}

		// Keep popping until there're no number greater than stack[i]
		while (stack[stack.length - 1] > num[i] && k > 0) {
			stack.pop();
			k--;
		}

		// Push the number
		stack.push(num[i]);
		i++;
	}

	// Pop if there's k left to use
	while (k > 0) {
		stack.pop();
		k--;
	}

	// Add the rest of the nums
	while (i < num.length) {
		stack.push(num[i]);
		i++;
	}

	// Remove leading zeroes
	// Why this method? There's a test case with number close to infinity that breaks type casting
	const res = stack.join("");
	let index = 0;
	while (index < res.length && res[index] === "0") {
		index++;
	}
	return res.slice(index) || "0";
}
