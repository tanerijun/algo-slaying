export function longestCommonPrefix(strs: string[]): string {
  if (strs.length === 0) {
    return "";
  }

  let out = "";
  let i = 0;

  while (checkSameLetter(strs, i)) {
    out += strs[0][i];
    i++;
  }

  return out;
};

function checkSameLetter(arr: string[], idx: number): boolean {
  const curr = arr[0][idx]

  if (!curr) {
    return false;
  }

  for (let i = 1; i < arr.length; i++) {
    if (arr[i][idx] != curr) {
      return false;
    }
  }

  return true;
}