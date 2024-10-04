function isPalindrome(s: string): boolean {
  const str = s.trim().toLowerCase().replace(/[\W_]/g, "");
  const strReverse = str.split("").reverse().join("");

  return str === strReverse;
}
// Time complexity: O(2 * n) = O(n)
// Space complexity: O(1)

function isPalindrome2(s: string): boolean {
  let l = 0;
  let r = s.length - 1;

  while (l < r) {
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
}
// Time complexity: O(n)
// Space complexity: O(1)
