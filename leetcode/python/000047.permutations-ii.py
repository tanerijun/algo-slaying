from collections import Counter


class Solution:
    # Time complexity: O(n * n!)
    # Space complexity: O(n)
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res, temp = [], []
        used = set()

        def backtrack():
            if len(temp) == len(nums):
                res.append(temp.copy())
                return

            for i in range(len(nums)):
                if i in used:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and i - 1 not in used:
                    continue
                used.add(i)
                temp.append(nums[i])
                backtrack()
                temp.pop()
                used.remove(i)

        backtrack()
        return res

    # Time complexity: O(n * n!)
    # Space complexity: O(n)
    def permuteUnique2(self, nums: list[int]) -> list[list[int]]:
        counter = Counter(nums)
        res, temp = [], []

        def backtrack():
            if len(temp) == len(nums):
                res.append(temp.copy())
                return

            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    temp.append(num)
                    backtrack()
                    temp.pop()
                    counter[num] += 1

        backtrack()
        return res
