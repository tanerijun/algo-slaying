function lengthOfLastWord(s: string): number {
	const str = s.trimEnd()
	let res = 0

	for (let i = str.length - 1; i >= 0; i--) {
		if (str[i] === " ") {
			break
		}
		res++
	}

	return res
}
// Time complexity: O(n)
// Space complexity: O(1)
