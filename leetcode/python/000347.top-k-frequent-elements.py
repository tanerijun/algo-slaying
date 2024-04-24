class Solution:
    # Time complexity: O(n log n)
    # Space complexity: O(n)
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        map: dict[int, int] = {}
        for n in nums:
            map[n] = map.get(n, 0) + 1

        items = sorted(map.items(), key=lambda t: t[1], reverse=True)

        res = []
        for i in range(k):
            res.append(items[i][0])

        return res
