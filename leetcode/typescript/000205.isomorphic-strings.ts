function isIsomorphic(s: string, t: string): boolean {
	if (s.length !== t.length) {
		return false
	}

	const mapS = new Map<string, string>()
	const mapT = new Map<string, string>()

	for (let i = 0; i < s.length; i++) {
		if (
			(mapS.has(s[i]) && mapS.get(s[i]) !== t[i]) ||
			(mapT.has(t[i]) && mapT.get(t[i]) !== s[i])
		) {
			return false
		}

		mapS.set(s[i], t[i])
		mapT.set(t[i], s[i])
	}

	return true
}
// Time complexity: O(n)
// Space complexity: O(n)

isIsomorphic("paper", "title")
