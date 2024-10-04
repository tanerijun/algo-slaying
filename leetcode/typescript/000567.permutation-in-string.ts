function checkInclusion(s1: string, s2: string): boolean {
  if (s1.length > s2.length) {
    return false;
  }

  const s1CharCount = new Array(26).fill(0);
  const windowCharCount = new Array(26).fill(0);

  for (let i = 0; i < s1.length; i++) {
    s1CharCount[s1[i].charCodeAt(0) - "a".charCodeAt(0)]++;
    windowCharCount[s2[i].charCodeAt(0) - "a".charCodeAt(0)]++;
  }

  let matches = 0;
  for (let i = 0; i < 26; i++) {
    if (s1CharCount[i] === windowCharCount[i]) {
      matches++;
    }
  }

  let l = 0;
  let r = s1.length;
  while (r < s2.length) {
    if (matches === 26) {
      return true;
    }

    let index = s2[r].charCodeAt(0) - "a".charCodeAt(0);
    windowCharCount[index]++;
    if (s1CharCount[index] === windowCharCount[index]) {
      matches++;
    } else if (s1CharCount[index] + 1 === windowCharCount[index]) {
      matches--;
    }

    index = s2[l].charCodeAt(0) - "a".charCodeAt(0);
    windowCharCount[index]--;
    if (s1CharCount[index] === windowCharCount[index]) {
      matches++;
    } else if (s1CharCount[index] - 1 === windowCharCount[index]) {
      matches--;
    }

    l++;
    r++;
  }

  return matches === 26;
}
// Time complexity: O(n)
// Space complexity: O(1)
