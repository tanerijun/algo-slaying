// Time complexity: O(2^n * n)
// Space complexity: O(n)
function partition(s: string): string[][] {
  const res: string[][] = [];
  const temp: string[] = [];

  function dfs(i: number) {
    if (i === s.length) {
      res.push([...temp]);
      return;
    }

    for (let j = i; j < s.length; j++) {
      const part = s.slice(i, j + 1);
      if (isPalindrome(part)) {
        temp.push(part);
        dfs(j + 1);
        temp.pop();
      }
    }
  }

  dfs(0);
  return res;
}

function isPalindrome(s: string) {
  let l = 0;
  let r = s.length - 1;

  while (l <= r) {
    if (s[l] !== s[r]) return false;
    l++;
    r--;
  }

  return true;
}
