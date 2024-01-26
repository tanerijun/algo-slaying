function numOfSubarrays(arr: number[], k: number, threshold: number): number {
	let res = 0

	let l = 0
	let r = l + k - 1
	let sum = arr.slice(l, r + 1).reduce((a, b) => a + b)
	if (sum / k >= threshold) {
		res++
	}

	while (r < arr.length - 1) {
		sum = sum - arr[l] + arr[r + 1]
		if (sum / k >= threshold) {
			res++
		}
		l++
		r++
	}

	return res
}
// Time complexity: O(n)
// Space complexity: O(1)
