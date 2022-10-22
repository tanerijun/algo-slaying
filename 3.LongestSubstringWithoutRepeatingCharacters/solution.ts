export function lengthOfLongestSubstring(s: string): number {
	let res = 0;
	const map = new Map<string, number>();

	for (let i = 0, j = 0; j < s.length; j++) {
		const char = map.get(s[j]);
		if (char) {
			i = Math.max(char, i);
		}
		map.set(s[j], j + 1);
		res = Math.max(res, j - i + 1);
	}

	return res;
}
