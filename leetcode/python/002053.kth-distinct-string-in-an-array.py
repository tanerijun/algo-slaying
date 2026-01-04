from collections import Counter


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def kthDistinct(self, arr: list[str], k: int) -> str:
        count = Counter(arr)
        for n, c in count.items():
            if c == 1:
                k -= 1
            if k == 0:
                return n
        return ""
