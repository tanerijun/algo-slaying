class NumArray:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def __init__(self, nums: list[int]):
        self.prefix_sum = []
        for n in nums:
            prev = self.prefix_sum[-1] if self.prefix_sum else 0
            self.prefix_sum.append(prev + n)

    # Time complexity: O(1)
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right] - (self.prefix_sum[left - 1] if left > 0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
