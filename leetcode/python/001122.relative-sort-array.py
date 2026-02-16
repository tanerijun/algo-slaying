from collections import Counter


class Solution:
    # Time complexity: O(n + m + n(log(n)))
    # Space complexity: O(n)
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        counter = Counter(arr1)

        res = []
        for n in arr2:
            res.extend([n] * counter.pop(n))

        for n in sorted(counter):
            res.extend([n] * counter.pop(n))

        return res
