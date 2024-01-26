// Brute force
// Time complexity: O(n)
// Space complexity: O(1)
function arrangeCoins(n: number): number {
	let row = 0;
	let i = 1;
	while (i <= n) {
		n -= i;
		row++;
		i++;
	}
	return row;
}

// Binary search
// Time complexity: O(n)
// Space complexity: O(1)
// Intuition:
// 		- We can find how many coins we need to create n row using Gauss Summation formula
// 		- Ex: To create 3 rows, we need: (n / 2) * (n + 1) coins = 1.5 * 4 coins = 6 coins
// 		- So, we use binary search and try to guess the rows
function arrangeCoins2(n: number): number {
	let l = 1;
	let r = n;

	while (l <= r) {
		const m = Math.floor((l + r) / 2);
		const coinsNeeded = (m / 2) * (m + 1);
		if (coinsNeeded < n) {
			l = m + 1;
		} else if (coinsNeeded > n) {
			r = m - 1;
		} else {
			return m;
		}
	}

	// Since we're here, it means there's excess coins, so we return r instead of l
	// because l is added by 1 before reaching this part.
	return r;
}
