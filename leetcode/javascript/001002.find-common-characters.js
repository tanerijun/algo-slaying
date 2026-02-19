/**
 * @param {string[]} words
 * @return {string[]}
 * Time complexity: O(n)
 * Space complexity: O(1) -> max 26
 */
var commonChars = function (words) {
  if (words.length === 1) {
    return words[0].split("");
  }

  const countMap = getCountMap(words[0]);
  for (let i = 1; i < words.length; i++) {
    const newCountMap = getCountMap(words[i]);

    for (const [k, v] of countMap.entries()) {
      countMap.set(k, Math.min(v, newCountMap.get(k) ?? 0));
    }
  }

  const res = [];

  for (const [k, v] of countMap.entries()) {
    for (let i = 0; i < v; i++) {
      res.push(k);
    }
  }

  return res;
};

function getCountMap(str) {
  const countMap = new Map();

  for (const ch of str) {
    countMap.set(ch, (countMap.get(ch) ?? 0) + 1);
  }

  return countMap;
}
