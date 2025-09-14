/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 * Time complexity: O(n(log(n)))
 * Space complexity: O(n)
 */
var kClosest = function(points, k) {
    points.sort((a, b) => (a[0] * a[0] + a[1] * a[1]) - (b[0] * b[0] + b[1] * b[1]));
    return points.slice(0, k);
};
