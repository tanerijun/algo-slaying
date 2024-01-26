function minWindow(s: string, t: string): string {
	let res = "";
	const sCountMap = new Map<string, number>();
	const tCountMap = new Map<string, number>();
	for (const char of t) {
		tCountMap.set(char, (tCountMap.get(char) ?? 0) + 1);
	}
	let have = 0;
	let need = tCountMap.size;
	let l = 0;

	for (let r = 0; r < s.length; r++) {
		if (tCountMap.has(s[r])) {
			sCountMap.set(s[r], (sCountMap.get(s[r]) ?? 0) + 1);

			if (sCountMap.get(s[r])! === tCountMap.get(s[r])) {
				have++;
			}
		}

		while (have === need) {
			const substring = s.slice(l, r + 1);

			if (res.length === 0 || substring.length < res.length) {
				res = substring;
			}

			if (tCountMap.has(s[l])) {
				sCountMap.set(s[l], sCountMap.get(s[l])! - 1);

				if (sCountMap.get(s[l])! < tCountMap.get(s[l])!) {
					have--;
				}
			}

			l++;
		}
	}

	return res;
}
// Time complexity: O(n)
// Space complexity: O(m) => m = t.length
