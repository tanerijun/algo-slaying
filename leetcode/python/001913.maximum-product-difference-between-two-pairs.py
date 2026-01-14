class Solution:
    # Time complexity: O(n(log(n)))
    # Space complexity: O(n) - PY uses Timsort
    def maxProductDifference(self, nums: list[int]) -> int:
        nums.sort()
        return (nums[-2] * nums[-1]) - (nums[0] * nums[1])

    # Time complexity: O(n)
    # Space complexity: O(1)
    def maxProductDifference2(self, nums: list[int]) -> int:
        biggest, second_biggest = 0, 0
        smallest, second_smallest = float("inf"), float("inf")

        for num in nums:
            if num > biggest:
                second_biggest = biggest
                biggest = num
            else:
                second_biggest = max(second_biggest, num)

            if num < smallest:
                second_smallest = smallest
                smallest = num
            else:
                second_smallest = min(second_smallest, num)

        return int(biggest * second_biggest - (smallest * second_smallest))
