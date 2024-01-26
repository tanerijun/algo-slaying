function isSubsequence(s: string, t: string): boolean {
	if (s.length === 0) return true

	let currentSIdx = 0

	for (let i = 0; i < t.length; i++) {
		const currentTarget = s[currentSIdx]

		if (t[i] === currentTarget) {
			currentSIdx++
			if (currentSIdx === s.length) {
				return true
			}
		}
	}

	return false
}
// Time complexity: O(n)
// Space complexity: O(1)
