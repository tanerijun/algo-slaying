/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 * Time complexity: O(log(min(m, n)))
 * Space complexity: O(1)
 */
var findMedianSortedArrays = function (nums1, nums2) {
  const total = nums1.length + nums2.length;

  if (nums1.length > nums2.length) {
    [nums1, nums2] = [nums2, nums1];
  }

  let l = 0;
  let r = nums1.length - 1;

  while (true) {
    const i = Math.floor((l + r) / 2);
    const j = Math.floor(total / 2) - i - 2;

    // The Infinity is necessary since i/j might be out of bounds
    const nums1Left = nums1[i] || -Infinity;
    const nums2Left = nums2[j] || -Infinity;
    const nums1Right = nums1[i + 1] || Infinity;
    const nums2Right = nums2[j + 1] || Infinity;

    // Partition is correct
    if (nums1Left <= nums2Right && nums2Left <= nums1Right) {
      // odd
      if (total % 2) {
        return Math.min(nums1Right, nums2Right);
      }
      // even
      return (Math.max(nums1Left, nums2Left) +
        Math.min(nums1Right, nums2Right)) / 2;
    }

    // Incorrect partition
    if (nums1Left > nums2Right) {
      r = i - 1;
    } else {
      l = i + 1;
    }
  }
};
