function angryProfessor(k: number, a: number[]): string {
	let onTime = 0
	let late = 0

	for (let i = 0; i < a.length; i++) {
		if (a[i] <= 0) {
			onTime++
		} else {
			late++
		}
	}

	if (onTime < k) {
		return "YES"
	} else {
		return "NO"
	}
}
