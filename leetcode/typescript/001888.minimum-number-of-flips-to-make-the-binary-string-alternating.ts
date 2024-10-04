function minFlips(s: string): number {
  const N = s.length;
  let ref1 = "0101010101";
  let ref2 = "1010101010";

  while (ref1.length < N * 2) {
    ref1 += ref1;
    ref2 += ref2;
  }

  let flipCountWithRef1 = 0;
  let flipCountWithRef2 = 0;

  for (let i = 0; i < N; i++) {
    if (s[i] !== ref1[i]) {
      flipCountWithRef1++;
    }
    if (s[i] !== ref2[i]) {
      flipCountWithRef2++;
    }
  }

  let res = Math.min(flipCountWithRef1, flipCountWithRef2);
  let l = 0;
  let r = N;

  // By the time r is equal to 2N, we have completed a full cycle
  while (r < N * 2) {
    if (s[l] !== ref1[l]) {
      flipCountWithRef1--;
    }
    if (s[l] !== ref2[l]) {
      flipCountWithRef2--;
    }

    // Move 1st char to the end
    s += s[l];
    l++;

    if (s[r] !== ref1[r]) {
      flipCountWithRef1++;
    }
    if (s[r] !== ref2[r]) {
      flipCountWithRef2++;
    }

    res = Math.min(res, flipCountWithRef1, flipCountWithRef2);
    r++;
  }

  return res;
}
// Time complexity: O(n) <-- But timeout on testcase where input is very big
// Space complexity: O(1)

// Slightly more optimized solution
function minFlips2(s: string): number {
  const N = s.length;
  let ref1 = "0101010101";
  let ref2 = "1010101010";

  while (ref1.length < N * 2) {
    ref1 += ref1;
    ref2 += ref2;
  }

  let flipCountWithRef1 = 0;
  let flipCountWithRef2 = 0;

  let res = Number.MAX_SAFE_INTEGER;
  let l = 0;
  s = s + s;

  for (let r = 0; r < s.length; r++) {
    if (s[r] !== ref1[r]) {
      flipCountWithRef1++;
    }
    if (s[r] !== ref2[r]) {
      flipCountWithRef2++;
    }

    // When window is too big
    if (r - l + 1 > N) {
      if (s[l] !== ref1[l]) {
        flipCountWithRef1--;
      }
      if (s[l] !== ref2[l]) {
        flipCountWithRef2--;
      }
      l++;
    }

    // Don't run when window is not yet created
    if (r - l + 1 === N) {
      res = Math.min(res, flipCountWithRef1, flipCountWithRef2);
    }
  }

  return res;
}
// Time complexity: O(n)
// Space complexity: O(1)
