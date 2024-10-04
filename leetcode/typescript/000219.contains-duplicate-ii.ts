function containsNearbyDuplicate(nums: number[], k: number): boolean {
  const map = new Map<number, number>();

  for (let i = 0; i < nums.length; i++) {
    const prevIndex = map.get(nums[i]);
    if (prevIndex !== undefined && i - prevIndex <= k) {
      return true;
    }
    map.set(nums[i], i);
  }

  return false;
}
// Time complexity: O(n)
// Space complexity: O(n)
