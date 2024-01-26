function maxVowels(s: string, k: number): number {
	let res = 0;
	let vowelCount = 0;
	let l = 0;

	for (let r = 0; r < s.length; r++) {
		if (r > k - 1) {
			if (isVowel(s[l])) {
				vowelCount--;
			}
			l++;
		}

		if (isVowel(s[r])) {
			vowelCount++;
		}

		res = Math.max(res, vowelCount);
	}

	return res;
}

function isVowel(c: string): boolean {
	return ["a", "e", "i", "o", "u"].includes(c);
}

// Time complexity: O(n)
// Space complexity: O(1)
