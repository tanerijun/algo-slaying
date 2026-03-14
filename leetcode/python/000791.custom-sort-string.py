from collections import Counter


class Solution:
    # Time complexity: O(n(log(n)))
    # Space complexity: O(n)
    def customSortString(self, order: str, s: str) -> str:
        rank_map = {c: i for i, c in enumerate(order)}
        return "".join(sorted(s, key=lambda x: rank_map.get(x, 26)))

    # Time complexity: O(n)
    # Space complexity: O(n)
    def customSortString2(self, order: str, s: str) -> str:
        s_counter = Counter(s)

        res = []
        for ch in order:
            res.append(ch * s_counter[ch])
            del s_counter[ch]

        for k, v in s_counter.items():
            res.append(k * v)

        return "".join(res)
