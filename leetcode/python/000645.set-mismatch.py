from collections import Counter


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def findErrorNums(self, nums: list[int]) -> list[int]:
        s = set()
        duplicate, missing = -1, -1

        for n in nums:
            if n in s:
                duplicate = n
            s.add(n)

        for i in range(1, len(nums) + 1):
            if i not in s:
                missing = i
                break

        return [duplicate, missing]

    # Time complexity: O(n)
    # Space complexity: O(n)
    def findErrorNums1(self, nums: list[int]) -> list[int]:
        counter = Counter(nums)

        duplicate, missing = -1, -1
        for i in range(1, len(nums) + 1):
            if counter[i] == 2:
                duplicate = i
            if counter[i] == 0:
                missing = i

        return [duplicate, missing]

    # Time complexity: O(n)
    # Space complexity: O(1)
    def findErrorNums2(self, nums: list[int]) -> list[int]:
        duplicate, missing = -1, -1

        for n in nums:
            n = abs(n)
            nums[n - 1] *= -1
            if nums[n - 1] > 0:
                duplicate = n

        for i, n in enumerate(nums):
            if n > 0 and i + 1 != duplicate:
                missing = i + 1
                break

        return [duplicate, missing]
