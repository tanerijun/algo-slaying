from collections import Counter, defaultdict


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def majorityElement(self, nums: list[int]) -> list[int]:
        threshold = len(nums) // 3
        count = Counter(nums)
        output = []
        for k, v in count.items():
            if v > threshold:
                output.append(k)
        return output

    # Time complexity: O(n)
    # Space complexity: O(1) -- hashmap size is at most 2
    # Since the threshold is n // 3, it's impossible for the output length to be more than 2 elements
    def majorityElement2(self, nums: list[int]) -> list[int]:
        threshold = len(nums) // 3
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

            if len(count) <= 2:
                continue

            # Remove all elements with 0 count
            new_count = defaultdict(int)
            for k, v in count.items():
                if v > 1:
                    new_count[k] = v - 1
            count = new_count

        res = []
        for k in count:  # will run at most 2x
            # This verification is important for this kind of test case:
            # [1, 2, 3, 4, 5, 6, 7, 8]
            if nums.count(k) > threshold:
                res.append(k)
        return res
