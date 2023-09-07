type Value = [number, string];

class TimeMap {
	map: Map<string, Array<Value>>;

	constructor() {
		this.map = new Map();
	}

	set(key: string, value: string, timestamp: number): void {
		// All the timestamps timestamp of set are strictly increasing.
		// So, we just have to push to the end of the array.
		// Otherwise, we'll have to look for the most suitable index so that our array is increasing
		// We need the array in sorted order, so that the get() function can run in O(log(n)) time

		const newVal: Value = [timestamp, value];

		const values = this.map.get(key);

		if (!values) {
			this.map.set(key, [newVal]);
			return;
		}

		values.push(newVal);
	}
	// Time complexity: O(1)

	get(key: string, timestamp: number): string {
		const values = this.map.get(key);
		if (!values) {
			return "";
		}

		let res: [number, number] | null = null; // [timestamp, index]
		let l = 0;
		let r = values.length - 1;

		while (l <= r) {
			const m = Math.floor((l + r) / 2);

			// Update res
			if (values[m][0] <= timestamp) {
				if (!res) {
					res = [values[m][0], m];
				} else {
					if ((values[m][0] > res[0]) || (values[m][0] === res[0] && m > res[1])) {
						res = [values[m][0], m];
					}
				}
			}

			if (values[m][0] <= timestamp) {
				l = m + 1;
			} else {
				r = m - 1;
			}
		}

		return res ? values[res[1]][1] : "";
	}
	// Time complexity: O(log(n))
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */
