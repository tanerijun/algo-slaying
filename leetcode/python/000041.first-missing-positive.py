class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def firstMissingPositive(self, nums: list[int]) -> int:
        candidates = set([i for i in range(1, len(nums) + 1)])
        for n in nums:
            if n in candidates:
                candidates.remove(n)
        return min(candidates) if candidates else len(nums) + 1

    # Time complexity: O(n)
    # Space complexity: O(n)
    def firstMissingPositive1(self, nums: list[int]) -> int:
        seen_positive = set()
        for n in nums:
            if n > 0:
                seen_positive.add(n)

        for i in range(1, len(nums) + 1):
            if i not in seen_positive:
                return i

        return len(nums) + 1

    # Time complexity: O(n)
    # Space complexity: O(1)
    def firstMissingPositive2(self, nums: list[int]) -> int:
        # Change all non-positives to positives that won't be considered
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = len(nums) + 1

        # Now that every number is positive, we can use negative as a seen mark
        # When reading, use abs to avoid the mark
        for i in range(len(nums)):
            if 1 <= abs(nums[i]) <= len(nums):
                if nums[abs(nums[i]) - 1] > 0:
                    nums[abs(nums[i]) - 1] *= -1

        # Find unmarked
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                return i

        # If we still haven't found the answer, then it's definitely the next positive number
        return len(nums) + 1
