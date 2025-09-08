/**
 * @param {string} s
 * @return {character}
 * Time complexity: O(1)
 * Space complexity: O(1)
 * Why not set? Because the length of seen is at most 26 (a-z)
 * Time complexity is also O(1) for the same reason
 */
var repeatedCharacter = function(s) {
  const seen = [];
  for (const ch of s) {
    if (seen.includes(ch)) return ch;
    seen.push(ch);
  }
};
