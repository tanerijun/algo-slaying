class Solution:
    # Bellman Ford
    # Time complexity: O(e * k)) - e: edges (number of flights), k: number of stops allowed
    # Space complexity: O(n)
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            temp = prices.copy()

            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < temp[d]:
                    temp[d] = prices[s] + p

            prices = temp

        return -1 if prices[dst] == float("inf") else int(prices[dst])
