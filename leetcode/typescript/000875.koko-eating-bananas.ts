function minEatingSpeed(piles: number[], h: number): number {
  let max = 0;
  for (const pile of piles) {
    max = Math.max(max, pile);
  }

  function getHours(banana: number) {
    let hours = 0;
    for (const pile of piles) {
      if (banana >= pile) {
        hours += 1;
      } else {
        hours += Math.ceil(pile / banana);
      }
    }

    return hours;
  }

  let res = Number.MAX_SAFE_INTEGER;
  let l = 1; // lower bound: eat 1 banana at a time
  let r = max; // upper bound: eat 1 pile at a time

  while (l <= r) {
    const m = Math.floor((l + r) / 2);
    const hours = getHours(m);

    if (hours > h) {
      l = m + 1;
    } else {
      res = m;
      r = m - 1;
    }
  }

  return res;
}
// Time complexity: O(n + n(log(m))) = O(n(1 + log(m)))
// Space complexity: O(1)
