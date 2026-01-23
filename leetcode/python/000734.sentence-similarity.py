from collections import defaultdict


class Solution:
    # Time complexity: O(n + m) -> n = len(sentences), m = len(similarPairs)
    # Space complexity: O(m)
    def areSentencesSimilar(
        self, sentence1: list[str], sentence2: list[str], similarPairs: list[list[str]]
    ) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        similarity_map = defaultdict(set)
        for w1, w2 in similarPairs:
            similarity_map[w1].add(w2)
            similarity_map[w2].add(w1)

        for w1, w2 in zip(sentence1, sentence2):
            if w1 == w2 or w2 in similarity_map[w1]:
                continue
            return False

        return True
