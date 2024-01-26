function longestCommonPrefix(strs: string[]): string {
	let res = ""

	loop: while (true) {
		const index = res.length
		const currentPrefix = strs[0][index]

		// Edge case: strs = [""]
		if (!currentPrefix) break loop

		for (let i = 1; i < strs.length; i++) {
			const str = strs[i]

			if (index === str.length) {
				break loop
			}

			if (str[index] !== currentPrefix) {
				break loop
			}
		}

		res += currentPrefix
	}

	return res
}
// Time complexity: O(n) - where n = the length of all the characters inside strs
// Best case:  Ω(n) - where n = length of the shortest string in strs
// Space complexity: O(1)
