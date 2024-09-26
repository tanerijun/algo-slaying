class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    # Time complexity: O(m), m being length of word
    # Space complexity: O(m)
    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if not c in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.isEnd = True

    # At each level, for a '.' character, we might need to explore up to 26 possibilities.
    # But on average, it's way better.
    # Time complexity: O(26^m).
    # Space complexity: O(m)
    def search(self, word: str) -> bool:
        def dfs(idx, root):
            cur = root

            for i in range(idx, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if not c in cur.children:
                        return False
                    cur = cur.children[c]

            return cur.isEnd

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
