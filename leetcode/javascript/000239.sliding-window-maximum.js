/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
var maxSlidingWindow = function (nums, k) {
  const output = [];
  const deque = new Deque();
  let l = 0;
  let r = 0;

  while (r < nums.length) {
    while (!deque.isEmpty() && nums[r] > deque.back()) {
      deque.popBack();
    }

    deque.pushBack(nums[r]);

    if (r + 1 >= k) {
      output.push(deque.front());

      if (nums[l] === deque.front()) {
        deque.popFront();
      }

      l++;
    }

    r++;
  }

  return output;
};
