// Time complexity: O(n * m * l) -> n = length of s, m = length of wordDict, l = length of longest word in wordDict
// Space complexity: O(n)
function wordBreak(s: string, wordDict: string[]): boolean {
  const dp = new Array(s.length + 1).fill(false); // can we break string up to index i?
  // The string at index 0 is an empty string,
  // To break it, just don't choose any word from wordDict.
  dp[0] = true;

  const wordSet = new Set(wordDict); // for O(1) look up

  let maxWordLength = 0;
  for (const word of wordDict) {
    maxWordLength = Math.max(maxWordLength, word.length);
  }

  for (let i = 1; i <= s.length; i++) {
    for (let j = i - 1; j >= Math.max(0, i - maxWordLength); j--) {
      // If word segment is in wordDict, we also check if the rest of the words is also segmentable (dp[j])
      if (wordSet.has(s.slice(j, i)) && dp[j]) {
        dp[i] = true;
        break;
      }
    }
  }

  return dp[s.length];
}
