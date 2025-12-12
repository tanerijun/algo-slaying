from collections import deque


class Solution:
    # Time complexity: O(n * l) -> l = length of the word
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        q = deque()
        q.append([beginWord, 1])

        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        while q:
            word, steps = q.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):
                for j in range(ord("a"), ord("z") + 1):
                    ch = chr(j)

                    if ch == word[i]:
                        continue

                    new_word = word[:i] + ch + word[i + 1 :]

                    if new_word in word_set:
                        word_set.remove(new_word)
                        q.append([new_word, steps + 1])

        return 0
