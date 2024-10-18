import heapq


class Solution:
    # Time complexity: O((n + k(log(n)))
    # Space complexity: O(1)
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]

    # Time complexity: O(n(log(k)))
    # Space complexity: O(n)
    def findKthLargest2(self, nums: list[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
        while len(heap) > k:
            heapq.heappop(heap)
        return heap[0]

    # Quick select
    # Time complexity: Worst -> O(n2), Average: O(n)
    # Space complexity:
    def findKthLargest3(self, nums: list[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)
