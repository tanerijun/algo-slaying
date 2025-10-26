var DetectSquares = function () {
  this.map = new Map();
};

/**
 * @param {number[]} point
 * @return {void}
 * Time complexity: O(1)
 * Space complexity: O(1)
 */
DetectSquares.prototype.add = function (point) {
  const key = point.join(",");
  this.map.set(key, (this.map.get(key) ?? 0) + 1);
};

/**
 * @param {number[]} point
 * @return {number}
 * Time complexity: O(n), n = size of the data structure
 * Space complexity: O(1)
 */
DetectSquares.prototype.count = function (point) {
  let res = 0;
  const [x, y] = point;

  for (const k of this.map.keys()) {
    const [px, py] = k.split(",").map(Number);
    if (px === x || py === y || Math.abs(py - y) !== Math.abs(px - x)) continue;
    res += (this.map.get([x, py].join(",")) ?? 0) *
      (this.map.get([px, y].join(",")) ?? 0) * this.map.get([px, py].join(","));
  }

  return res;
};

/**
 * Your DetectSquares object will be instantiated and called as such:
 * var obj = new DetectSquares()
 * obj.add(point)
 * var param_2 = obj.count(point)
 */
