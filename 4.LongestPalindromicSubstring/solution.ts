function expandAroundCenter(s: string, l: number, r: number): number {

	while (l >= 0 && r < s.length && s[l] === s[r]) {
		l--;
		r++;
	}

	return r - l - 1;
}

export function longestPalindrome(s: string): string {
	if (s.length <= 1) return s;

	// Keep track of the answer
	let lIdx = 0;
	let rIdx = 0;

	for (let i = 0; i < s.length; i++) {
		let caseOdd = expandAroundCenter(s, i, i); // ex: babad
		let caseEven = expandAroundCenter(s, i, i + 1); // ex: abbd
		const len = Math.max(caseOdd, caseEven);
		if (len > rIdx - lIdx) {
			lIdx = i - Math.floor((len - 1) / 2);
			rIdx = i + Math.floor(len / 2);
		}
	}

	return s.slice(lIdx, rIdx + 1);
}