class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def buyChoco(self, prices: list[int], money: int) -> int:
        cheapest, second_cheapest = float("inf"), float("inf")
        for price in prices:
            if price < cheapest:
                second_cheapest = cheapest
                cheapest = price
            else:
                second_cheapest = min(second_cheapest, price)

        leftover = money - cheapest - second_cheapest
        return money if leftover < 0 else int(leftover)
