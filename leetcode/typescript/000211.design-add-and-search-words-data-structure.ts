class TrieNode {
  children: Map<string, TrieNode>;
  isEnd: boolean;

  constructor() {
    this.children = new Map();
    this.isEnd = false;
  }
}

class WordDictionary {
  root: TrieNode;

  constructor() {
    this.root = new TrieNode();
  }

  // Time complexity: O(n) -- n = word length
  // Space complexity: O(n)
  addWord(word: string): void {
    let cur = this.root;
    for (const c of word) {
      if (!cur.children.has(c)) {
        cur.children.set(c, new TrieNode());
      }
      cur = cur.children.get(c)!;
    }
    cur.isEnd = true;
  }

  // Time complexity: O(26^m) -- m = word length. Worst case is when all chars of the word are "."
  // Space complexity: O(m)
  search(word: string): boolean {
    function dfs(idx: number, root: TrieNode): boolean {
      let cur = root;
      for (let i = idx; i < word.length; i++) {
        const c = word[i];
        if (c == ".") {
          for (const child of cur.children.values()) {
            if (dfs(i + 1, child)) return true;
          }
          return false;
        }
        if (!cur.children.has(c)) return false;
        cur = cur.children.get(c)!;
      }
      return cur.isEnd;
    }

    return dfs(0, this.root);
  }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
