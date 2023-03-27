function bonAppetit(bill: number[], k: number, b: number): void {
	let sumOfFoodAnnaAlsoEat = 0
	for (let i = 0; i < bill.length; i++) {
		if (i === k) {
			continue
		}

		sumOfFoodAnnaAlsoEat += bill[i]
	}

	const amountAnnaShouldPay = sumOfFoodAnnaAlsoEat / 2
	if (amountAnnaShouldPay === b) {
		console.log("Bon Appetit")
	} else {
		console.log(b - amountAnnaShouldPay)
	}
}

// Time complexity: O(n)
