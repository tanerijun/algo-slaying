export function convert(s: string, numRows: number): string {
	const resArr: string[] = Array(numRows).fill('');
	let cursor: number = 0;
	let isDecreasing: boolean = false;

	for (let i = 0; i < s.length; i++) {
		resArr[cursor] += s[i];

		if (cursor === 0) {
			isDecreasing = false;
		}

		if (cursor === numRows - 1) {
			isDecreasing = true;
		}

		if (isDecreasing) {
			if (cursor != 0) cursor -= 1;
		} else {
			cursor += 1;
		}
	}

	return resArr.join('');
}
