// Time complexity: O(n)
// Space complexity: O(1)
function longestPalindrome(s: string): string {
  let output = "";

  function findPalindrome(l: number, r: number) {
    let length = 0;

    while (l >= 0 && r < s.length && s[l] === s[r]) {
      length++;
      l--;
      r++;
    }

    const palindrome = s.slice(l + 1, r);
    if (palindrome.length > output.length) {
      output = palindrome;
    }
  }

  for (let i = 0; i < s.length; i++) {
    findPalindrome(i, i);
    findPalindrome(i, i + 1);
  }

  return output;
}
