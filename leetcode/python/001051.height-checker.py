class Solution:
    # Time complexity: O(n(log(n)))
    # Space complexity: O(n)
    def heightChecker(self, heights: list[int]) -> int:
        expected = sorted(heights)
        res = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1
        return res

    # Time complexity: O(n + k) -> k == range of numbers
    # Space complexity: O(n + k)
    # Count sort
    def heightChecker1(self, heights: list[int]) -> int:
        max_height = 100
        count = [0] * (max_height + 1)  # Space O(k)
        for h in heights:  # O(n)
            count[h] += 1

        expected = []  # Space O(n)
        for h in range(1, max_height + 1):  # O(n + k)
            c = count[h]
            for _ in range(c):
                expected.append(h)

        res = 0
        for i in range(len(heights)):  # O(n)
            if heights[i] != expected[i]:
                res += 1

        return res
