class Solution:
    # Time complexity: O(n * m)
    # Space complexity: O(1)
    def firstPalindrome(self, words: list[str]) -> str:
        def is_palindrome(word: str) -> bool:
            i, j = 0, len(word) - 1
            while i <= j:
                if word[i] != word[j]:
                    return False
                i += 1
                j -= 1
            return True

        for word in words:
            if is_palindrome(word):
                return word
        return ""
