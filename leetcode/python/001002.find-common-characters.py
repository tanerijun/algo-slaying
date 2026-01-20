from collections import Counter


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def commonChars(self, words: list[str]) -> list[str]:
        counters = [Counter(w) for w in words]
        res = []
        for i in range(ord("a"), ord("z") + 1):
            ch = chr(i)
            count = float("inf")
            for counter in counters:
                count = min(count, counter[ch])
            if count > 0:
                for _ in range(int(count)):
                    res.append(ch)
        return res

    # Time complexity: O(n)
    # Space complexity: O(n)
    def commonChars1(self, words: list[str]) -> list[str]:
        counters = [Counter(w) for w in words]
        res = []
        for i in range(ord("a"), ord("z") + 1):
            ch = chr(i)
            count = min([counter[ch] for counter in counters])
            if count > 0:
                res.extend([ch] * count)
        return res

    # Time complexity: O(n)
    # Space complexity: O(1) -> max 26
    def commonChars2(self, words: list[str]) -> list[str]:
        counter = Counter(words[0])

        for word in words:
            cur_counter = Counter(word)
            for c in counter:
                counter[c] = min(counter[c], cur_counter[c])

        res = []
        for c in counter:
            res.extend([c] * counter[c])

        return res
