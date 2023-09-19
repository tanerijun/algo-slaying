// Floyd's cycle detection algorithm
function findDuplicate(nums: number[]): number {
	let slow = 0;
	let fast = 0;

	while (true) {
		slow = nums[slow];
		fast = nums[nums[fast]]; // twice as fast as slow

		if (slow === fast) {
			break;
		}
	}

	// At this point, we know where fast and slow intersect
	// Now, we create another pointer from the start,
	// And advancing it together with the slow pointer.
	// When they meet, that's the cycle start

	let slow2 = 0;

	while (true) {
		slow = nums[slow];
		slow2 = nums[slow2];

		if (slow === slow2) {
			return slow;
		}
	}
}
// Time complexity: O(n)
// Space complexity: O(1)

// Using extra space
function findDuplicate2(nums: number[]): number {
	const set = new Set<number>();

	for (const num of nums) {
		if (set.has(num)) {
			return num;
		}

		set.add(num);
	}

	return -1; // won't happen
}
// Time complexity: O(n)
// Space complexity: O(n)

// Marking visited value within the array
function findDuplicate3(nums: number[]): number {
	for (const num of nums) {
		const idx = Math.abs(num);

		if (nums[idx] < 0) {
			return idx;
		}

		nums[idx] = -nums[idx];
	}

	return -1; // won't happen
}
// Time complexity: O(n)
// Space complexity: O(1)
