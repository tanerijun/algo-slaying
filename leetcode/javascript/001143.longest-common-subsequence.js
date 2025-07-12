/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 * Time complexity: O(m * n)
 * Space complexity: O(m * n)
 */
var longestCommonSubsequence = function (text1, text2) {
  const dp = Array.from(
    { length: text1.length + 1 },
    (_, i) => Array(text2.length + 1).fill(0),
  );

  for (let i = text1.length - 1; i >= 0; i--) {
    for (let j = text2.length - 1; j >= 0; j--) {
      if (text1[i] === text2[j]) {
        dp[i][j] = 1 + dp[i + 1][j + 1];
      } else {
        dp[i][j] = Math.max(dp[i + 1][j], dp[i][j + 1]);
      }
    }
  }

  return dp[0][0];
};
