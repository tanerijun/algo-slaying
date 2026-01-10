from collections import Counter, defaultdict


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def numIdenticalPairs(self, nums: list[int]) -> int:
        counter = Counter(nums)
        res = 0
        for v in counter.values():
            if v > 1:
                res += (v * (v - 1)) / 2  # C(n, 2)
        return int(res)

    # Time complexity: O(n)
    # Space complexity: O(n)
    # As we traverse the array, each new occurrence of a value
    # can form a good pair with every previous occurrence of that same value.
    def numIdenticalPairs2(self, nums: list[int]) -> int:
        counter = defaultdict(int)
        res = 0
        for n in nums:
            res += counter[n]
            counter[n] += 1
        return res
