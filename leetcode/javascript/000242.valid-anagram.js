/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
var isAnagram = function (s, t) {
  const counter = new Map();

  for (const ch of s) {
    const cur = counter.get(ch) ?? 0;
    counter.set(ch, cur + 1);
  }

  for (const ch of t) {
    const cur = counter.get(ch) ?? 0;
    counter.set(ch, cur - 1);
  }

  for (const val of counter.values()) {
    if (val !== 0) return false;
  }

  return true;
};
