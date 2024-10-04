function searchRange(nums: number[], target: number): number[] {
  const leftBoundary = binarySearch(nums, target, "left");
  const rightBoundary = binarySearch(nums, target, "right");

  return [leftBoundary, rightBoundary];
}

function binarySearch(
  nums: number[],
  target: number,
  searchDir: "left" | "right",
) {
  let res = -1;
  let l = 0;
  let r = nums.length - 1;

  while (l <= r) {
    const m = Math.floor((l + r) / 2);

    // Standard binary search
    if (target > nums[m]) {
      l = m + 1;
    } else if (target < nums[m]) {
      r = m - 1;
    } else {
      res = m;

      // But we don't stop here, we need to find the boundary
      if (searchDir === "left") {
        r = m - 1;
      } else if (searchDir === "right") {
        l = m + 1;
      }
    }
  }

  return res;
}
// Time complexity: O(log(n))
// Space complexity: O(1)
