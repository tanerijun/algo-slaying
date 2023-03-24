function kangaroo(x1: number, v1: number, x2: number, v2: number): string {
	if (v1 > v2) {
		while (x1 <= x2) {
			if (x1 === x2) {
				return "YES"
			}

			x1 += v1
			x2 += v2
		}
	}

	return "NO"
}

// kangaroo(0, 3, 4, 2) // (4 - 0) / (3 - 2) = 4
// kangaroo(1, 2, 1000, 1) // (1000 - 1) / (2 - 1) = 999
// kangaroo(3, 6, 3553, 2) // (3553 - 3) / (6 - 2) = 887
// Time complexity: O(x2 - x1 / v1 - v2)

function kangaroo2(x1: number, v1: number, x2: number, v2: number): string {
	if (v1 > v2 && (x2 - x1) % (v1 - v2) === 0) {
		return "YES"
	}

	return "NO"
}

// Time complexity: O(1)
// Just check if on the worst case (see kangaroo fn above), the division result in 0 or not
