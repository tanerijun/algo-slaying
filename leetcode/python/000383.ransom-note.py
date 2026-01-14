from collections import Counter


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1) - max length 26
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counter = Counter(magazine)
        for ch in ransomNote:
            if magazine_counter[ch] == 0:
                return False
            magazine_counter[ch] -= 1
        return True
