function totalFruit(fruits: number[]): number {
	let countMap = new Map<number, number>();
	let l = 0;
	let total = 0;
	let max = 0;
	for (let r = 0; r < fruits.length; r++) {
		countMap.set(fruits[r], (countMap.get(fruits[r]) ?? 0) + 1);
		total++;

		while (countMap.size > 2) {
			const fruit = fruits[l];
			countMap.set(fruit, countMap.get(fruit)! - 1);
			total--;
			l++;
			if (countMap.get(fruit) === 0) {
				countMap.delete(fruit);
			}
		}

		max = Math.max(max, total);
	}

	return max;
}
// Time complexity: O(n)
// Space complexity: O(1)
