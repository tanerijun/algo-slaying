function successfulPairs(spells: number[], potions: number[], success: number): number[] {
	let res: number[] = [];
	potions.sort((a, b) => a - b);

	function countSuccesses(spell: number) {
		let res = 0;
		let l = 0;
		let r = potions.length - 1;

		while (l <= r) {
			const m = Math.floor((l + r) / 2);
			const product = spell * potions[m];

			if (product >= success) {
				res = potions.length - m;
				r = m - 1;
			} else {
				l = m + 1;
			}
		}

		return res;
	}

	for (const spell of spells) {
		const successCount = countSuccesses(spell);
		res.push(successCount);
	}

	return res;
}
// Time complexity: O(m(log(m)) + n(log(m))) = O((m + n) log m) -- m = potions.length, n = spells.length
// Space complexity: O(1)
