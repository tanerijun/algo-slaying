function wordPattern(pattern: string, s: string): boolean {
	const charToWordMap = new Map<string, string>()
	const mappedWords = new Set<string>()
	const words = s.split(" ")

	if (pattern.length !== words.length) {
		return false
	}

	for (let i = 0; i < pattern.length; i++) {
		if (!charToWordMap.has(pattern[i])) {
			if (mappedWords.has(words[i])) {
				return false
			}

			charToWordMap.set(pattern[i], words[i])
			mappedWords.add(words[i])
		}

		const mappedWord = charToWordMap.get(pattern[i])
		if (mappedWord !== words[i]) {
			return false
		}
	}

	return true
}
// Time complexity: O(n)
// Space complexity: O(n)
