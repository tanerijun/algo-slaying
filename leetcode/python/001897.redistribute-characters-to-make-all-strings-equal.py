from collections import Counter


class Solution:
    # Time complexity: O(n) -> total number of characters
    # Space complexity: O(1) -> max 26
    def makeEqual(self, words: list[str]) -> bool:
        counter = Counter()
        for word in words:
            counter.update(word)
        for v in counter.values():
            if v % len(words) != 0:
                return False
        return True
