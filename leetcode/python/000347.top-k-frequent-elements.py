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


class Solution2:
    # Using a variation of bucket sort
    # Time complexity: O(n)
    # Space complexity: O(n)
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count: dict[int, int] = {}
        freq: list[list[int]] = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, c in count.items():
            freq[c].append(n)

        res: list[int] = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


## IN PROGRESS
