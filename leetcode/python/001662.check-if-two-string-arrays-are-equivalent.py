class Solution:
    # Time complexity: O(n + m)
    # Space complexity: O(n + m)
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        return "".join(word1) == "".join(word2)

    # Time complexity: O(n + m)
    # Space complexity: O(1)
    def arrayStringsAreEqual1(self, word1: list[str], word2: list[str]) -> bool:
        w1_idx = w2_idx = i = j = 0

        while w1_idx < len(word1) and w2_idx < len(word2):
            if word1[w1_idx][i] != word2[w2_idx][j]:
                return False

            i += 1
            j += 1

            if i == len(word1[w1_idx]):
                w1_idx += 1
                i = 0
            if j == len(word2[w2_idx]):
                w2_idx += 1
                j = 0

        return w1_idx == len(word1) and w2_idx == len(word2)
