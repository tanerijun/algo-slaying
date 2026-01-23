class Solution:
    # Time complexity: O(n * m)
    # Space complexity: O(n * m)
    def validWordSquare(self, words: list[str]) -> bool:
        v_words = []
        for c in range(len(words[0])):
            word = ""
            for r in range(len(words)):
                if c < len(words[r]):
                    word += words[r][c]
                else:
                    break
            v_words.append(word)

        for w, vw in zip(words, v_words):
            if w != vw:
                return False

        return True

    # Time complexity: O(n * m)
    # Space complexity: O(1)
    def validWordSquare1(self, words: list[str]) -> bool:
        for i in range(len(words)):
            for j in range(len(words[i])):
                # missing mirrored row or missing mirrored column or not matching
                if j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False

        return True
