function find132pattern(nums: number[]): boolean {
	const stack: Array<[number, number]> = []; // [num, currMin], a monotonic decreasing stack
	let min = nums[0];
	for (let num of nums.slice(1)) {
		// Maintain monotonic decreasing property of the stack by
		// popping until the stack is empty or if the top of the stack is number bigger than "num".
		// In the 1 3 2 pattern, 3 is bigger than 2
		while (stack.length > 0 && num >= stack[stack.length - 1][0]) {
			stack.pop();
		}

		// After popping, the number at the top of the stack, will be greater than the current num, if the stack is not empty.'
		if (stack.length > 0 && num > stack[stack.length - 1][1]) {
			return true;
		}

		// If it's empty or if the min up to the num at the top of the stack is <= current num
		stack.push([num, min]);
		min = Math.min(min, num);
	}
	return false;
}
// Time complexity: O(n)
// Space complexity: O(n)
