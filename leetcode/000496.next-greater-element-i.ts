function nextGreaterElement(nums1: number[], nums2: number[]): number[] {
	// All integers in nums1 and nums2 are unique.
	// All the integers of nums1 also appear in nums2.

	const res: number[] = []

	// Store index of each num in nums2 in a hashmap
	const indexMap = new Map<number, number>()
	for (let i = 0; i < nums2.length; i++) {
		indexMap.set(nums2[i], i)
	}

	for (let i = 0; i < nums1.length; i++) {
		const index = indexMap.get(nums1[i]) as number
		let nextGreater = -1

		for (let j = index + 1; j < nums2.length; j++) {
			if (nums2[j] > nums1[i]) {
				nextGreater = nums2[j]
				break
			}
		}

		res.push(nextGreater)
	}

	return res
}
// Time complexity: O(n * m)
// Space complexity: O(n)
