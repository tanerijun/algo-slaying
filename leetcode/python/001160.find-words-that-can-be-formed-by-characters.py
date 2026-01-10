from collections import Counter


class Solution:
    # Time complexity: O(n + (m * k)) -> n = len(chars), m = len(words), k = avg word length
    # Space complexity: O(1) -> max map size is 26
    def countCharacters(self, words: list[str], chars: str) -> int:
        res = 0
        c1 = Counter(chars)
        for word in words:
            c2 = Counter(word)
            is_good = True

            for ch in c2:
                if c1[ch] < c2[ch]:
                    is_good = False
                    break

            if is_good:
                res += len(word)

        return res
