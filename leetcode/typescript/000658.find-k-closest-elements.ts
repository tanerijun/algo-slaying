function findClosestElements(arr: number[], k: number, x: number): number[] {
	let m = findIndexOfElementWithClosestValue(arr, x, 0, arr.length - 1);
	let left: number[] = [];
	let right: number[] = [arr[m]];
	let l = m - 1;
	let r = m + 1;

	for (let i = 1; i < k; i++) {
		if (l < 0) {
			right = right.concat(arr.slice(r, r + k - i));
			break;
		}

		if (r > arr.length - 1) {
			left = arr.slice(l - (k - i - 1), l + 1).concat(left);
			break;
		}

		if (x - arr[l] <= arr[r] - x) {
			left = [arr[l]].concat(left);
			l--;
		} else {
			right.push(arr[r]);
			r++;
		}
	}

	return left.concat(right);
}

function findIndexOfElementWithClosestValue(arr: number[], x: number, l: number, r: number) {
	while (l < r) {
		if (r - l === 1) {
			return Math.abs(x - arr[l]) <= Math.abs(x - arr[r]) ? l : r;
		}
		const mid = l + Math.floor((r - l) / 2);
		if (arr[mid] < x) {
			l = mid;
		} else if (arr[mid] > x) {
			r = mid;
		} else {
			return mid;
		}
	}

	return r;
}

// Time complexity: O(log(n) + k)
// Space complexity: O(k)
