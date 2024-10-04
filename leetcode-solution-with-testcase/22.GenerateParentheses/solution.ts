export function generateParenthesis(n: number): string[] {
  const res: string[] = [];
  backtrack(res, "", 0, 0, n);
  return res;
}

function backtrack(
  ans: String[],
  cur: String,
  open: number,
  close: number,
  max: number,
) {
  // max * 2 is max length of the string
  // ex: if n = 3, then the possible string: "((()))", "(()())", "(())()", "()(())", "()()()"
  // are all of length n * 2 = 6
  if (cur.length === max * 2) {
    ans.push(cur);
    return;
  }

  // The max amounts of "(" is n
  if (open < max) {
    backtrack(ans, cur + "(", open + 1, close, max);
  }

  // There shouldn't be more ")" than "("
  if (close < open) {
    backtrack(ans, cur + ")", open, close + 1, max);
  }
}
