/**
 Do not return anything, modify nums in-place instead.
 */
function moveZeroes(nums: number[]): void {
	let l = 0
	for (let r = 0; r < nums.length; r++) {
		if (nums[r] !== 0) {
			const temp = nums[l]
			nums[l] = nums[r]
			nums[r] = temp
			l++
		}
	}
}
// Time complexity: O(n)
// Space complexity: O(1)
