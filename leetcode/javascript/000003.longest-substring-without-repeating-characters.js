/**
 * @param {string} s
 * @return {number}
 * Time complexity: O(n)
 * Space complexity: O(m) -> m = unique chars in s
 */
var lengthOfLongestSubstring = function (s) {
  const charSet = new Set();
  let l = 0;
  let res = 0;

  for (let r = 0; r < s.length; r++) {
    while (charSet.has(s[r])) {
      charSet.delete(s[l]);
      l++;
    }

    charSet.add(s[r]);
    res = Math.max(res, r - l + 1);
  }

  return res;
};
