/**
 * @param {string[]} names
 * @param {number[]} heights
 * @return {string[]}
 * Time complexity: O(n(log(n)))
 * Space complexity: O(n)
 */
var sortPeople = function (names, heights) {
  return names.map((name, i) => [name, heights[i]])
    .sort((a, b) => b[1] - a[1]) // descending
    .map(([name]) => name);
};
