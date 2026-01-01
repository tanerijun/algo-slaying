from collections import Counter


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def majorityElement(self, nums: list[int]) -> int:
        count = Counter(nums)
        most_common = max(count.values())
        for k, v in count.items():
            if v == most_common:
                return k
        return 0  # won't happen

    # Time complexity: O(n)
    # Space complexity: O(1)
    def majorityElement1(self, nums: list[int]) -> int:
        count, res = 1, nums[0]
        for n in nums[1:]:
            if count == 0:
                res = n
            if n == res:
                count += 1
            else:
                count -= 1
        return res
