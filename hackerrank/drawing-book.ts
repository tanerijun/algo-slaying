function pageCount(n: number, p: number): number {
	const pageCountFromEnd = n - p + 1
	const shouldStartFromEnd = pageCountFromEnd <= p
	const hasUnpairedPage = !shouldStartFromEnd || n % 2 === 0

	if (shouldStartFromEnd) {
		p = pageCountFromEnd
	}

	if (hasUnpairedPage) {
		return Math.floor(p / 2)
	} else {
		return Math.ceil(p / 2) - 1
	}
}
