/**
 * @param {string} s
 * @return {boolean}
 * Time complexity: O(n)
 * Space complexity: O(1)
 */
var isPalindrome = function (s) {
  let l = 0;
  let r = s.length - 1;

  while (l <= r) {
    if (!/[a-zA-Z0-9]/.test(s[l])) {
      l++;
      continue;
    }
    if (!/[a-zA-Z0-9]/.test(s[r])) {
      r--;
      continue;
    }
    if (s[l].toLowerCase() !== s[r].toLowerCase()) {
      return false;
    }
    l++;
    r--;
  }

  return true;
};
