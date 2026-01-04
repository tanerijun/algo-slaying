class Solution:
    # Time complexity: O(n^2 * m^2)
    # Space complexity: O(1)
    def stringMatching(self, words: list[str]) -> list[str]:
        res = []
        for w1 in words:
            for w2 in words:
                if w1 == w2:
                    continue
                else:
                    if w1 in w2:
                        res.append(w1)
                        break
        return res

    # Time complexity: O(n^2 * m^2)
    # Space complexity: O(1)
    def stringMatching1(self, words: list[str]) -> list[str]:
        words.sort(key=len)
        res = []
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    res.append(words[i])
                    break
        return res
