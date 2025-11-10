import heapq


class Solution(object):
    # Time complexity: O(nlog(n))
    # Space complexity: O(n)
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first = min_heap[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    # Slight optimization: early return
                    # If the element we want to pop is not the min,
                    # It will create gap.
                    # For example: If we still have 1, and we pop 2 (groupSize 3)
                    # It'll be impossible to construct [1, 2, 3] later
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)

        return True
