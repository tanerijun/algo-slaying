function numRescueBoats(people: number[], limit: number): number {
  people.sort((a, b) => a - b);

  let boatCount = 0;
  let currentLimit = limit;
  let l = 0;
  let r = people.length - 1;

  while (l <= r) {
    boatCount++;
    currentLimit -= people[r];

    if (currentLimit > 0 && currentLimit - people[l] >= 0) {
      currentLimit -= people[l];
      l++;
    }

    r--;
    currentLimit = limit;
  }

  return boatCount;
}
// Time complexity: O(n*log(n))
// Space complexity: O(1)
