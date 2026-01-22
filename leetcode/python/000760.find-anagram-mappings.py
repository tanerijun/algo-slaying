class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def anagramMappings(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums2_idx_map = {}
        for i in range(len(nums2)):
            nums2_idx_map[nums2[i]] = i
        return [nums2_idx_map[n] for n in nums1]
