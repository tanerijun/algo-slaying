class Solution:
    # Time complexity: O(n + m) -> len(words) + len(queries)
    # Space complexity: O(n)
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        def check_vowel_string(s):
            vowels = ["a", "e", "i", "o", "u"]
            return s[0] in vowels and s[-1] in vowels

        prefix_sum = [int(check_vowel_string(words[0]))]
        for i in range(1, len(words)):
            prefix_sum.append(prefix_sum[-1] + int(check_vowel_string(words[i])))

        res = []
        for l, r in queries:
            res.append(prefix_sum[r] - (prefix_sum[l - 1] if l > 0 else 0))

        return res

    # Time complexity: O(n + m) -> len(words) + len(queries)
    # Space complexity: O(n)
    # Optimized v0
    def vowelStrings1(self, words: list[str], queries: list[list[int]]) -> list[int]:
        vowels = set(["a", "e", "i", "o", "u"])

        def is_valid(s):
            return 1 if (s[0] in vowels and s[-1] in vowels) else 0

        prefix_sum = [0] * (len(words) + 1)  # pad with 0 to handle l = 0
        for i in range(len(words)):
            prefix_sum[i + 1] = prefix_sum[i] + is_valid(words[i])

        res = []
        for l, r in queries:
            res.append(prefix_sum[r + 1] - prefix_sum[l])

        return res
