function maxProfit(prices: number[]): number {
  let profit = 0;
  let currMin = Number.MAX_VALUE;
  let currMax = 0;

  for (const price of prices) {
    if (!currMax && price <= currMin) {
      // Find best buying time
      // !currMax is necessary to trigger the second conditional after best buying time is decided
      currMin = price;
    } else if (price > currMax) {
      // Find best selling time
      // This section run until we find a price that's smaller than currMax,
      // which means that it's time to sell, and buy the new low
      currMax = price;
    } else {
      // Found ideal buying and selling day
      // Because this section only trigger when stock price drop lower than the one on best selling day
      profit += currMax - currMin;
      currMin = price; // buy the new low
      currMax = 0; // reset best selling day, and decide after we buy a stock again
    }
  }

  if (currMax > 0) {
    profit += currMax - currMin;
  }

  return profit;
}

// Time complexity: O(n)
// Space complexity: O(1)
