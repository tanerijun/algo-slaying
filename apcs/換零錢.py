# 可憐的貝茜在Slobbovia邊境的便利商店工作。Slobbovian國的人使用與美國不同的幣值，而且幣值隨時在更動！
# 請你幫助貝茜做出最佳情況硬幣數給Slobbovian顧客。你需要用N（1<=N<=10）種不同的硬幣數提供C（1≦C≦1000）分錢給顧客。你可以假設所有的測資都是可以用此N種硬幣提供出來的。
# 舉例:如果有5種不同的幣值50，25，10，5，1可用，貝茜將找出93分錢的最佳情況硬幣數（最少的硬幣），用1個50，1個25，1個10，1個5，3個1的硬幣（共7個硬幣）為最佳硬幣數。
# 那能有多難呢？最後兩個測資較具有挑戰性。

# Input
# 每筆測資的第1行有兩數字C與N，其中用一個空格隔開
# 接下來的第2到第N+1行為各種不同的幣值

# Output
# 輸出最佳情況硬幣數

# Sample Input #1
# 93 5
# 25
# 50
# 10
# 1
# 5

# Sample Output #1
# 7


def count_coin_needed(change, coins):
    # Initialize the dp array with a large value
    # Each index i in this arr will represent the minimum number of coins needed to make amount i.
    dp = [float("inf")] * (change + 1)
    dp[0] = 0

    # Build the dp array
    for i in range(1, change + 1):
        for coin in coins:
            if coin <= i:
                # Example:
                # Let's say we're trying to make 7 cents, and we're considering a 5-cent coin.
                # i is 7 (we're working on making 7 cents)
                # coin is 5 (we're considering the 5-cent coin)
                # dp[7] might currently be 7 (using all 1-cent coins)
                # dp[2] (which is dp[7 - 5]) might be 2 (two 1-cent coins)
                # So the calc below will be:
                # dp[7] = min(dp[7], dp[7 - 5] + 1) = min(7, 2 + 1) = min(7, 3) = 3
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[change] if dp[change] != float("inf") else -1


def main():
    C, N = map(int, input().split())
    coins = []
    for _ in range(N):
        coins.append(int(input()))
    print(count_coin_needed(C, coins))


if __name__ == "__main__":
    main()
