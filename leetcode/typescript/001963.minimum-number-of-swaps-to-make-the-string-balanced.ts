function minSwaps(s: string): number {
  let close = 0; // add 1 for every "]" and subtract 1 for every "["
  let maxClose = 0; // the number of swap to make

  for (const c of s) {
    if (c === "[") {
      close--;
    } else {
      close++;
    }
    maxClose = Math.max(close, maxClose);
  }

  // Every swap get rid of 2 bracket
  // e.g ]]], say that we swap the first bracket
  // []], notice how the first and second bracket is now considered balanced
  return Math.ceil(maxClose / 2);
}
// Time complexity: O(n)
// Space complexity: O(1)
