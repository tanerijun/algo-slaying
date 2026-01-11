class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(n)
    def getRow(self, rowIndex: int) -> list[int]:
        res = [1]

        for _ in range(rowIndex):
            next = [0] * (len(res) + 1)
            for i in range(len(res)):
                next[i] += res[i]
                next[i + 1] += res[i]
            res = next

        return res
