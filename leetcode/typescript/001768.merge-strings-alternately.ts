function mergeAlternately(word1: string, word2: string): string {
  let res = "";
  const shorterWord = word1.length < word2.length ? word1 : word2;
  const longerWord = shorterWord == word1 ? word2 : word1;

  for (let i = 0; i < shorterWord.length; i++) {
    res += word1[i];
    res += word2[i];
  }

  res += longerWord.slice(shorterWord.length);

  return res;
}
// Time complexity: O(n)
// Space complexity: O(1)
