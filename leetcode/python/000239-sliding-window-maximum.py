from collections import deque


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output = []
        q = deque()
        l = r = 0

        while r < len(nums):
            while q and q[-1] < nums[r]:
                q.pop()

            q.append(nums[r])

            if (r + 1) >= k:
                output.append(q[0])

                if nums[l] == q[0]:
                    q.popleft()

                l += 1

            r += 1

        return output
