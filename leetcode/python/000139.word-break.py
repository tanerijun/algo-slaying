class Solution:
    # Time complexity: O(n * l^2) -> n == len(wordDict), l == max_word_len
    # Space complexity: O(n)
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        word_set = set(wordDict)
        max_word_len = max([len(w) for w in wordDict])

        for i in range(1, len(s) + 1):
            for j in range(i - 1, max(0, i - max_word_len) - 1, -1):
                if s[j:i] in word_set and dp[j]:
                    dp[i] = True
                    break

        return dp[len(s)]
