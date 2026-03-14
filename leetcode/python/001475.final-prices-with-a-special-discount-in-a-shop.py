class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    def finalPrices(self, prices: list[int]) -> list[int]:
        res = []
        for i in range(len(prices)):
            res.append(prices[i])
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    res[i] = prices[i] - prices[j]
                    break
        return res

    # Time complexity: O(n)
    # Space complexity: O(n)
    def finalPrices2(self, prices: list[int]) -> list[int]:
        res = [prices[0]]
        stack = [0]

        for i in range(1, len(prices)):
            res.append(prices[i])
            while stack and prices[i] <= prices[stack[-1]]:
                idx = stack.pop()
                res[idx] -= prices[i]
            stack.append(i)

        return res
