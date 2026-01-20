from collections import Counter


class Solution:
    # Time complexity: O(n + m)
    # Space complexity: O(n + m)
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1_counter = Counter(nums1)
        nums2_counter = Counter(nums2)

        ref = nums1 if len(nums1) < len(nums2) else nums2

        res = set()
        for n in ref:
            if nums1_counter[n] and nums2_counter[n]:
                res.add(n)
        return list(res)

    # Time complexity: O(n + m)
    # Space complexity: O(n + m)
    def intersection1(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1, set2 = set(nums1), set(nums2)
        ref = set1 if len(set1) < len(set2) else set2
        res = []
        for n in ref:
            if n in set1 and n in set2:
                res.append(n)
        return res

    # Time complexity: O(n + m)
    # Space complexity: O(n + m)
    def intersection2(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1, set2 = set(nums1), set(nums2)
        return list(set1.intersection(set2))

    # Time complexity: O(n + m)
    # Space complexity: O(n)
    def intersection3(self, nums1: list[int], nums2: list[int]) -> list[int]:
        seen = set(nums1)
        res = []
        for n in nums2:
            if n in seen:
                res.append(n)
                seen.remove(n)
        return res
