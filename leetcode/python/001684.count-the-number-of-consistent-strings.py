class Solution:
    # Time complexity: O(n * m) -> n = len(words), m = len of the longest word
    # Space complexity: O(l) -> l = length of allowed string
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        res = 0
        allowed_set = set(allowed)
        for word in words:
            is_consistent = True
            for ch in word:
                if ch not in allowed_set:
                    is_consistent = False
                    break
            if is_consistent:
                res += 1
        return res
