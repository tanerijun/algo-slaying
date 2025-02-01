// Time complexity: O(2^n)
// Space complexity: O(n)
function subsetsWithDup(nums: number[]): number[][] {
  const res: number[][] = [];
  const temp: number[] = [];
  nums.sort();

  function dfs(i: number) {
    if (i === nums.length) {
      res.push([...temp]);
      return;
    }

    temp.push(nums[i]);
    dfs(i + 1);

    temp.pop();
    while (i < nums.length && nums[i] === nums[i + 1]) {
      i++;
    }
    dfs(i + 1);
  }

  dfs(0);
  return res;
}
