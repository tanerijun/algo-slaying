class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def check(self, nums: list[int]) -> bool:
        N = len(nums)
        smallest = min(nums)
        smallest_idx = nums.index(smallest)

        smallest_count = 1
        if smallest_idx == 0:
            for i in range(N - 1, -1, -1):
                if nums[i] == smallest:
                    smallest_count += 1
                else:
                    break

        prev = smallest
        idx = (smallest_idx + 1) % N
        k = N - smallest_count
        while k > 0:
            if nums[idx % N] < prev:
                return False
            prev = nums[idx % N]
            idx += 1
            k -= 1
        return True

    # Time complexity: O(n)
    # Space complexity: O(1)
    # Cleaned up
    def check1(self, nums: list[int]) -> bool:
        N = len(nums)
        pivot_count = 0

        for i in range(N):
            # Count how many times we have a "drop" (pivot point)
            if nums[i] > nums[(i + 1) % N]:
                pivot_count += 1

        # A sorted rotated array has at most 1 pivot point
        # (0 pivots means it's already sorted, 1 pivot means it's rotated)
        return pivot_count <= 1
