function countPalindromicSubsequence(s: string): number {
	const uniquePalindromeSet = new Set<string>()
	const charIndexMap = new Map<string, number[]>()

	for (let i = 0; i < s.length; i++) {
		const indexes = charIndexMap.get(s[i]) ?? []
		indexes.push(i)
		charIndexMap.set(s[i], indexes)
	}

	for (const [k, v] of charIndexMap) {
		if (v.length === 1) {
			continue
		}

		for (let j = v[0] + 1; j <= v[v.length - 1] - 1; j++) {
			uniquePalindromeSet.add(k + s[j] + k)
		}
	}

	return uniquePalindromeSet.size
}
// Time complexity: O(n + mn) m = number of unique characters
// Space complexity: O(n)
