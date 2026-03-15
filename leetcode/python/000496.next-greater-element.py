class Solution:
    # Time complexity: O(n) + O(m)
    # Space complexity: O(m)
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nextGreaterMap = {n: -1 for n in nums2}
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                popped_n = stack.pop()
                nextGreaterMap[popped_n] = nums2[i]
            stack.append(nums2[i])

        return [nextGreaterMap[n] for n in nums1]
