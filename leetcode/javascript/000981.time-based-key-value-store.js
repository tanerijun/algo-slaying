var TimeMap = function () {
  this.map = new Map();
};

/**
 * @param {string} key
 * @param {string} value
 * @param {number} timestamp
 * @return {void}
 * Note: timestamp is strictly increasing
 * Time complexity: O(1)
 */
TimeMap.prototype.set = function (key, value, timestamp) {
  if (!this.map.has(key)) {
    this.map.set(key, []);
  }

  const values = this.map.get(key);
  values.push([timestamp, value]);
  this.map.set(key, values);
};

/**
 * @param {string} key
 * @param {number} timestamp
 * @return {string}
 * Time complexity: O(log(n))
 */
TimeMap.prototype.get = function (key, timestamp) {
  const vals = this.map.get(key);
  if (!vals) return "";

  let left = 0;
  let right = vals.length - 1;
  let potentialAnswer;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (vals[mid][0] === timestamp) {
      return vals[mid][1];
    }

    if (vals[mid][0] < timestamp) {
      potentialAnswer = vals[mid][1];
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return potentialAnswer || "";
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */
