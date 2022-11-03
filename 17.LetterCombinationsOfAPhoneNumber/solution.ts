export function letterCombinations(digits: string): string[] {
  const res: string[] = [];
  const digitToLettersMap = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "qprs",
    "8": "tuv",
    "9": "wxyz"
  }

  function backtrack(i: number, curr: string) {
    if (curr.length === digits.length) {
      res.push(curr);
      return;
    }

    const letters = digitToLettersMap[digits[i] as keyof typeof digitToLettersMap];

    for (const letter of letters) {
      backtrack(i + 1, curr + letter);
    }
  }

  if (digits) {
    backtrack(0, "");
  }

  return res;
};