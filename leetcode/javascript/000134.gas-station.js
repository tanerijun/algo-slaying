/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 * Time complexity: O(n)
 * Space complexity: O(1)
 */
var canCompleteCircuit = function (gas, cost) {
  const gasSum = gas.reduce((acc, val) => acc + val, 0);
  const costSum = cost.reduce((acc, val) => acc + val, 0);
  if (gasSum < costSum) return -1;

  // At this point, we know that a solution exist for sure
  // And the solution is unique (according to the problem statement)
  // Hint: If we start from station a and get stuck at station b,
  // then NO station between a and b can reach b either.
  // Proof: When traveling from a→b, we accumulate some surplus gas before
  // reaching any intermediate station x. If we start fresh from x instead,
  // we begin with 0 surplus (less gas than we had when passing through x
  // from a). Since we couldn't reach b with MORE gas, we definitely can't
  // reach it with LESS gas. Therefore, we can skip all stations between
  // a and b, and try starting from b+1.
  // If station a itself is negative, we fail immediately and skip it
  let total = 0;
  let res = 0;
  for (let i = 0; i < gas.length; i++) {
    total += gas[i] - cost[i];
    if (total < 0) {
      total = 0;
      res = i + 1;
    }
  }

  return res;
};
