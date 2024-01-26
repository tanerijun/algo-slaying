function numSubseq(nums: number[], target: number): number {
	const MOD = 1_000_000_007

	let answer = 0
	nums.sort((a, b) => a - b)

	// Precompute the value of 2 to the power of each value.
	// The standard 2 ** i -- will break when i >= 1024
	const power: number[] = []
	power[0] = 1
	for (let i = 1; i < nums.length; i++) {
		power[i] = (power[i - 1] * 2) % MOD
	}

	let l = 0
	let r = nums.length - 1
	while (l <= r) {
		if (nums[l] + nums[r] > target) {
			r--
			continue
		}

		answer += power[r - l]
		answer %= MOD
		l++
	}

	return answer
}
