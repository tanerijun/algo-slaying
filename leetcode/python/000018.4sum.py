class Solution:
    # Time complexity: O(n^3)
    # Space complexity: O(1)
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        res, temp = [], []

        def kSum(k, start, target):
            if k == 2:
                l, r = start, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        res.append(temp + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
            else:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    temp.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    temp.pop()

        kSum(4, 0, target)
        return res
