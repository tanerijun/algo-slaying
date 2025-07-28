/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 * Time complexity: O(n)
 * Space complexity: O(1)
 */
var checkInclusion = function (s1, s2) {
  if (s1.length > s2.length) return false;

  const s1CharMap = createAlphabetMap();
  const s2CharMap = createAlphabetMap();

  for (let i = 0; i < s1.length; i++) {
    s1CharMap[s1[i]]++;
    s2CharMap[s2[i]]++;
  }

  let matches = 0;
  for (const [key, val] of Object.entries(s1CharMap)) {
    if (val === s2CharMap[key]) matches++;
  }

  if (matches === 26) return true;

  let l = 0;
  let r = s1.length;
  while (r < s2.length) {
    const rightChar = s2[r];
    if (s1CharMap[rightChar] === s2CharMap[rightChar]) {
      matches--;
    }
    s2CharMap[rightChar]++;
    if (s1CharMap[rightChar] === s2CharMap[rightChar]) {
      matches++;
    }

    const leftChar = s2[l];
    if (s1CharMap[leftChar] === s2CharMap[leftChar]) {
      matches--;
    }
    s2CharMap[leftChar]--;
    if (s1CharMap[leftChar] === s2CharMap[leftChar]) {
      matches++;
    }

    if (matches === 26) return true;

    l++;
    r++;
  }

  return false;
};

function createAlphabetMap() {
  const map = {};
  for (let i = "a".charCodeAt(0); i <= "z".charCodeAt(0); i++) {
    map[String.fromCharCode(i)] = 0;
  }
  return map;
}
