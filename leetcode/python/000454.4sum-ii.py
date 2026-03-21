class Solution:
    # Time complexity: O(n^4)
    # Space complexity: O(1)
    def fourSumCount(
        self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]
    ) -> int:
        count = 0
        for n1 in nums1:
            for n2 in nums2:
                for n3 in nums3:
                    for n4 in nums4:
                        if n1 + n2 + n3 + n4 == 0:
                            count += 1
        return count

    # Time complexity: O(n^3)
    # Space complexity: O(n)
    # The innermost loop over nums4 is just asking "does any value in nums4 equal -(n1+n2+n3)?"
    # We can answer that in O(1) with a hashmap.
    def fourSumCount2(
        self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]
    ) -> int:
        count4 = {}
        for n in nums4:
            count4[n] = count4.get(n, 0) + 1

        count = 0
        for n1 in nums1:
            for n2 in nums2:
                for n3 in nums3:
                    count += count4.get(-(n1 + n2 + n3), 0)

        return count

    # Time complexity: O(n^3)
    # Space complexity: O(n)
    #
    def fourSumCount3(
        self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]
    ) -> int:
        count4 = {}
        for n in nums4:
            count4[n] = count4.get(n, 0) + 1

        count = 0
        for n1 in nums1:
            for n2 in nums2:
                for n3 in nums3:
                    count += count4.get(-(n1 + n2 + n3), 0)

        return count

    # Time complexity: O(n^2)
    # Space complexity: O(n^2)
    #
    def fourSumCount4(
        self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]
    ) -> int:
        count34 = {}
        for n3 in nums3:
            for n4 in nums4:
                count34[n3 + n4] = count34.get(n3 + n4, 0) + 1

        count = 0
        for n1 in nums1:
            for n2 in nums2:
                count += count34.get(-(n1 + n2), 0)

        return count
