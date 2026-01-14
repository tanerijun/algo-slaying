class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        for i in range(len(words)):
            if words[i][-1] != words[(i + 1) % len(words)][0]:
                return False
        return True

    # Time complexity: O(n)
    # Space complexity: O(1)
    def isCircularSentence2(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        for i in range(len(sentence)):
            if sentence[i] == " ":
                if sentence[i - 1] != sentence[i + 1]:
                    return False
        return True
