class Solution:
    # Time complexity: O(n2)
    # Space complexity: O(n)
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]

        for _ in range(numRows - 1):
            prev = [0] + res[-1] + [0]
            next = []
            for i in range(len(res[-1]) + 1):
                next.append(prev[i] + prev[i + 1])
            res.append(next)

        return res
