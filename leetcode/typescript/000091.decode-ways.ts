// Time complexity: O(n)
// Space complexity: O(n)
function numDecodings(s: string): number {
  const dp0 = 1; // if s is of length 0, there is only 1 way to decode (which is by doing nothing)
  const dp1 = s[0] === "0" ? 0 : 1; // it's not possible to decode string that start with 0
  const dp: number[] = [dp0, dp1]; // represents number of way to decode when string is of length i

  for (let i = 2; i <= s.length; i++) {
    let waysToDecode = 0;

    // New single digit is valid
    if (s[i - 1] !== "0") {
      waysToDecode += dp[i - 1];
    }

    // Last 2 digit is valid
    if (
      Number(s.slice(i - 2, i)) >= 10 && Number(s.slice(i - 2, i)) <= 26
    ) {
      waysToDecode += dp[i - 2];
    }

    dp[i] = waysToDecode;
  }

  return dp[dp.length - 1];
}

// Time complexity: O(n)
// Space complexity: O(1)
// Notice that in the first solution, we only need to keep track of dp[i-1] and dp[i-2].
// Based on this, we can optimize the space complexity to O(1)
function numDecodings2(s: string): number {
  let dpTwoPrev = 1;
  let dpOnePrev = s[0] === "0" ? 0 : 1;

  for (let i = 2; i <= s.length; i++) {
    let waysToDecode = 0;

    // New single digit is valid
    if (s[i - 1] !== "0") {
      waysToDecode += dpOnePrev;
    }

    // Last 2 digit is valid
    if (
      Number(s.slice(i - 2, i)) >= 10 && Number(s.slice(i - 2, i)) <= 26
    ) {
      waysToDecode += dpTwoPrev;
    }

    dpTwoPrev = dpOnePrev;
    dpOnePrev = waysToDecode;
  }

  return dpOnePrev;
}

function numDecodings3(s: string): number {
  if (s[0] === "0") return 0;

  let dpTwoPrev = 1; // ways to decode up to prev 2 pos, ways to decode empty string,
  let dpOnePrev = 1; // ways to decode up to prev 1 pos, ways to decode with just the first digit

  for (let i = 1; i < s.length; i++) {
    let ways = 0;

    if (s[i] !== "0") {
      ways += dpOnePrev;
    }

    if (
      Number(s.slice(i - 1, i + 1)) >= 10 && Number(s.slice(i - 1, i + 1)) <= 26
    ) {
      ways += dpTwoPrev;
    }

    dpTwoPrev = dpOnePrev;
    dpOnePrev = ways;
  }

  return dpOnePrev;
}
