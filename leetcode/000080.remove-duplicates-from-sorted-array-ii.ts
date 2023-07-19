function removeDuplicates(nums: number[]): number {
	const currentNumber = {
		value: nums[0],
		count: 1,
	}

	let idx = 1

	for (let i = 1; i < nums.length; i++) {
		if (currentNumber.count < 2 && nums[i] === currentNumber.value) {
			currentNumber.count++

			const temp = nums[idx]
			nums[idx] = nums[i]
			nums[i] = temp

			idx++
		} else if (nums[i] !== currentNumber.value) {
			currentNumber.count = 1
			currentNumber.value = nums[i]

			const temp = nums[idx]
			nums[idx] = nums[i]
			nums[i] = temp

			idx++
		}
	}

	return idx
}
